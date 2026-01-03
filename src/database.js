// 导入所需模块
const sqlite3 = require("sqlite3").verbose(); // SQLite数据库模块
const path = require("path"); // 路径处理模块
const fs = require("fs-extra"); // 文件系统模块（扩展版）
const crypto = require("crypto"); // 加密模块

/**
 * 递归获取指定目录下的所有JSON文件
 * @param {string} dir - 要搜索的目录路径
 * @returns {Promise<Array<string>>} - JSON文件路径数组
 */
async function getAllJsonFiles(dir) {
  let results = [];
  // 读取目录内容，包含文件类型信息
  const items = await fs.readdir(dir, { withFileTypes: true });
  
  for (const item of items) {
    const full = path.join(dir, item.name); // 构建完整文件路径
    
    if (item.isDirectory()) {
      // 如果是目录，递归搜索
      results = results.concat(await getAllJsonFiles(full));
    } else if (item.isFile() && full.endsWith(".json")) {
      // 如果是JSON文件，添加到结果数组
      results.push(full);
    }
  }
  
  return results;
}
/**
 * 工作流数据库类 - 管理n8n工作流的数据库操作
 */
class WorkflowDatabase {
  /**
   * 创建工作流数据库实例
   * @param {string} dbPath - 数据库文件路径，默认值为 "database/workflows.db"
   */
  constructor(dbPath = "database/workflows.db") {
    this.dbPath = dbPath; // 数据库文件路径
    this.workflowsDir = "workflows"; // 工作流文件存储目录
    this.db = null; // 数据库连接对象
    this.initialized = false; // 初始化状态标志
  }

  /**
   * 初始化数据库连接和表结构
   * @returns {Promise<void>}
   */
  async initialize() {
    // 如果已经初始化，直接返回
    if (this.initialized) return;
    
    // 初始化数据库
    await this.initDatabase();
    
    // 标记为已初始化
    this.initialized = true;
  }

  /**
   * 初始化数据库连接和配置
   * @returns {Promise<void>}
   */
  async initDatabase() {
    // 确保数据库目录存在
    const dbDir = path.dirname(this.dbPath);
    await fs.ensureDir(dbDir);

    return new Promise((resolve, reject) => {
      // 创建数据库连接
      this.db = new sqlite3.Database(this.dbPath, (err) => {
        if (err) {
          reject(err);
          return;
        }

        // 配置数据库参数以提高性能
        this.db.run("PRAGMA journal_mode=WAL"); // 启用WAL模式（提高并发性能）
        this.db.run("PRAGMA synchronous=NORMAL"); // 设置同步模式为NORMAL（平衡性能和安全性）
        this.db.run("PRAGMA cache_size=10000"); // 设置缓存大小为10000页
        this.db.run("PRAGMA temp_store=MEMORY"); // 将临时表存储在内存中

        // 创建数据库表
        this.createTables().then(resolve).catch(reject);
      });
    });
  }

  /**
   * 创建数据库表结构
   * @returns {Promise<void>}
   */
  async createTables() {
    // 创建数据库表
    return new Promise((resolve, reject) => {
      const queries = [
        // 主工作流表
        `CREATE TABLE IF NOT EXISTS workflows (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          filename TEXT UNIQUE NOT NULL,
          name TEXT NOT NULL,
          folder TEXT DEFAULT '',
          workflow_id TEXT,
          active BOOLEAN DEFAULT 0,
          description TEXT,
          trigger_type TEXT,
          complexity TEXT,
          node_count INTEGER DEFAULT 0,
          integrations TEXT,
          tags TEXT,
          created_at TEXT,
          updated_at TEXT,
          file_hash TEXT,
          file_size INTEGER,
          analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )`,

        // FTS5全文搜索表（简化版）
        `CREATE VIRTUAL TABLE IF NOT EXISTS workflows_fts USING fts5(
          filename,
          name,
          description,
          integrations,
          tags
        )`,

        // 性能优化索引
        "CREATE INDEX IF NOT EXISTS idx_trigger_type ON workflows(trigger_type)",
        "CREATE INDEX IF NOT EXISTS idx_complexity ON workflows(complexity)",
        "CREATE INDEX IF NOT EXISTS idx_active ON workflows(active)",
        "CREATE INDEX IF NOT EXISTS idx_node_count ON workflows(node_count)",
        "CREATE INDEX IF NOT EXISTS idx_filename ON workflows(filename)",

        // 同步FTS表的触发器（简化版）
        // 插入后触发器
        `CREATE TRIGGER IF NOT EXISTS workflows_ai AFTER INSERT ON workflows BEGIN
          INSERT INTO workflows_fts(filename, name, description, integrations, tags)
          VALUES (new.filename, new.name, new.description, new.integrations, new.tags);
        END`,

        // 删除后触发器
        `CREATE TRIGGER IF NOT EXISTS workflows_ad AFTER DELETE ON workflows BEGIN
          DELETE FROM workflows_fts WHERE filename = old.filename;
        END`,

        // 更新后触发器
        `CREATE TRIGGER IF NOT EXISTS workflows_au AFTER UPDATE ON workflows BEGIN
          DELETE FROM workflows_fts WHERE filename = old.filename;
          INSERT INTO workflows_fts(filename, name, description, integrations, tags)
          VALUES (new.filename, new.name, new.description, new.integrations, new.tags);
        END`,
      ];

      // 顺序执行查询以避免竞争条件
      const runQuery = (index) => {
        if (index >= queries.length) {
          resolve();
          return;
        }

        const query = queries[index];
        this.db.run(query, (err) => {
          if (err) {
            console.error(`查询 ${index + 1} 出错:`, err.message);
            reject(err);
            return;
          }
          // 执行下一个查询
          runQuery(index + 1);
        });
      };

      // 开始执行第一个查询
      runQuery(0);
    });
  }

  /**
   * 计算文件的MD5哈希值
   * @param {string} filePath - 文件路径
   * @returns {string} - MD5哈希值（十六进制字符串）
   */
  getFileHash(filePath) {
    // 读取文件内容
    const buffer = fs.readFileSync(filePath);
    // 计算并返回MD5哈希值
    return crypto.createHash("md5").update(buffer).digest("hex");
  }

  /**
   * 格式化工作流名称（从文件名转换为易读的名称）
   * @param {string} filename - 工作流文件名
   * @returns {string} - 格式化后的工作流名称
   */
  formatWorkflowName(filename) {
    // 移除.json扩展名并按下划线分割
    const name = filename.replace(".json", "");
    const parts = name.split("_");

    // 如果第一部分只是数字，则跳过
    const startIndex = parts[0] && /^\d+$/.test(parts[0]) ? 1 : 0;
    const cleanParts = parts.slice(startIndex);

    // 格式化每个部分
    return cleanParts
      .map((part) => {
        const lower = part.toLowerCase();
        
        // 特殊术语映射（保持大写格式）
        const specialTerms = {
          http: "HTTP",
          api: "API",
          webhook: "Webhook",
          automation: "Automation",
          automate: "Automate",
          scheduled: "Scheduled",
          triggered: "Triggered",
          manual: "Manual",
        };

        // 如果是特殊术语，使用预定义格式，否则首字母大写
        return (
          specialTerms[lower] || part.charAt(0).toUpperCase() + part.slice(1)
        );
      })
      .join(" "); // 用空格连接所有部分
  }

  /**
   * 分析工作流文件内容，提取关键信息
   * @param {string} filePath - 工作流文件路径
   * @returns {Object|null} - 工作流信息对象，如果分析失败则返回null
   */
  analyzeWorkflow(filePath) {
    try {
      // 读取工作流JSON数据
      const data = fs.readJsonSync(filePath);
      
      // 提取基本文件信息
      const filename = path.basename(filePath); // 文件名
      const fileSize = fs.statSync(filePath).size; // 文件大小
      const fileHash = this.getFileHash(filePath); // 文件哈希值

      // 确定工作流所属文件夹
      const rel = path.relative(this.workflowsDir, filePath);
      const parts = rel.split(path.sep);
      const folder = parts.length > 1 ? parts[0] : "";

      // 构建工作流基本信息对象
      const workflow = {
        filename, // 文件名
        name: this.formatWorkflowName(filename), // 格式化的工作流名称
        folder, // 所属文件夹
        workflow_id: data.id || "", // 工作流ID
        active: data.active || false, // 是否激活
        nodes: data.nodes || [], // 节点列表
        connections: data.connections || {}, // 连接关系
        tags: data.tags || [], // 标签列表
        created_at: data.createdAt || "", // 创建时间
        updated_at: data.updatedAt || "", // 更新时间
        file_hash: fileHash, // 文件哈希值
        file_size: fileSize, // 文件大小
      };

      // 如果JSON数据中有更有意义的名称，则使用该名称
      const jsonName = data.name?.trim();
      if (
        jsonName &&
        jsonName !== filename.replace(".json", "") &&
        !jsonName.startsWith("My workflow") // 排除默认的"My workflow"名称
      ) {
        workflow.name = jsonName;
      }

      // 分析节点数量
      const nodeCount = workflow.nodes.length;
      workflow.node_count = nodeCount;

      // 确定工作流复杂度
      if (nodeCount <= 5) {
        workflow.complexity = "low"; // 低复杂度（≤5个节点）
      } else if (nodeCount <= 15) {
        workflow.complexity = "medium"; // 中等复杂度（6-15个节点）
      } else {
        workflow.complexity = "high"; // 高复杂度（>15个节点）
      }

      // 分析触发类型和集成
      const { triggerType, integrations } = this.analyzeNodes(workflow.nodes);
      workflow.trigger_type = triggerType;
      workflow.integrations = Array.from(integrations);

      // 生成工作流描述
      workflow.description = this.generateDescription(
        workflow,
        triggerType,
        integrations
      );

      return workflow;
    } catch (error) {
      console.error(
        `分析工作流文件 "${filePath}" 出错: ${error.message}`
      );
      return null;
    }
  }

  /**
   * 分析工作流节点，确定触发类型和集成列表
   * @param {Array} nodes - 工作流节点列表
   * @returns {Object} - 包含triggerType和integrations的对象
   */
  analyzeNodes(nodes) {
    const integrations = new Set(); // 集成集合（去重）
    let triggerType = "Manual"; // 默认触发类型为手动

    // 遍历所有节点
    nodes.forEach((node) => {
      const nodeType = node.type || "";

      // 从节点类型中提取集成名称
      if (nodeType.includes(".")) {
        const parts = nodeType.split(".");
        if (parts.length >= 2) {
          const integration = parts[1];
          // 排除core和base集成（这些是内置组件）
          if (integration !== "core" && integration !== "base") {
            integrations.add(
              integration.charAt(0).toUpperCase() + integration.slice(1) // 首字母大写
            );
          }
        }
      }

      // 根据节点类型确定触发类型
      if (nodeType.includes("webhook")) {
        triggerType = "Webhook"; // Webhook触发
      } else if (nodeType.includes("cron") || nodeType.includes("schedule")) {
        triggerType = "Scheduled"; // 定时触发
      } else if (nodeType.includes("trigger")) {
        triggerType = "Triggered"; // 事件触发
      }
    });

    return { triggerType, integrations };
  }

  /**
   * 生成工作流描述
   * @param {Object} workflow - 工作流信息对象
   * @param {string} triggerType - 触发类型
   * @param {Set} integrations - 集成集合
   * @returns {string} - 工作流描述
   */
  generateDescription(workflow, triggerType, integrations) {
    const parts = [];

    // 添加触发类型信息
    if (triggerType !== "Manual") {
      parts.push(`${triggerType} 工作流`);
    } else {
      parts.push("手动工作流");
    }

    // 添加集成信息
    if (integrations.size > 0) {
      // 只显示前3个集成，其余用"+n more"表示
      const integrationList = Array.from(integrations).slice(0, 3);
      if (integrations.size > 3) {
        integrationList.push(`+${integrations.size - 3} 个更多`);
      }
      parts.push(`集成 ${integrationList.join(", ")}`);
    }

    // 添加复杂度信息
    parts.push(
      `包含 ${workflow.node_count} 个节点（${workflow.complexity} 复杂度）`
    );

    return parts.join(" ");
  }

  /**
   * 索引所有工作流文件，将它们的信息存储到数据库中
   * @param {boolean} forceReindex - 是否强制重新索引，即使文件哈希未变化
   * @returns {Promise<Object>} - 索引结果统计信息
   */
  async indexWorkflows(forceReindex = false) {
    // 确保数据库已初始化
    if (!this.initialized) {
      await this.initialize();
    }

    // 获取所有工作流JSON文件
    const jsonFiles = await getAllJsonFiles(this.workflowsDir);

    let processed = 0; // 处理的文件数
    let skipped = 0; // 跳过的文件数（未变化）
    let errors = 0; // 错误的文件数

    // 遍历所有工作流文件
    for (const filePath of jsonFiles) {
      // 分析工作流文件
      const workflow = this.analyzeWorkflow(filePath);

      // 如果分析失败，记录错误并继续
      if (!workflow) {
        errors++;
        continue;
      }

      try {
        // 检查数据库中是否已存在该工作流
        const existing = await this.getWorkflowByFilename(workflow.filename);
        
        // 如果未强制重新索引，且文件内容未变化，则跳过
        if (
          !forceReindex &&
          existing &&
          existing.file_hash === workflow.file_hash
        ) {
          skipped++;
          continue;
        }

        // 更新或插入工作流信息到数据库
        await this.upsertWorkflow(workflow);
        processed++;
      } catch (error) {
        console.error(
          `索引工作流 ${workflow.filename} 出错: ${error.message}`
        );
        errors++;
      }
    }

    // 返回索引结果统计
    return { processed, skipped, errors, total: jsonFiles.length };
  }

  /**
   * 根据文件名获取工作流信息
   * @param {string} filename - 工作流文件名
   * @returns {Promise<Object|null>} - 工作流信息对象，如果不存在则返回null
   */
  async getWorkflowByFilename(filename) {
    return new Promise((resolve, reject) => {
      this.db.get(
        "SELECT * FROM workflows WHERE filename = ?",
        [filename],
        (err, row) => {
          if (err) reject(err);
          else resolve(row);
        }
      );
    });
  }

  /**
   * 更新或插入工作流信息到数据库
   * @param {Object} workflow - 工作流信息对象
   * @returns {Promise<number>} - 插入或更新的记录ID
   */
  async upsertWorkflow(workflow) {
    return new Promise((resolve, reject) => {
      // 准备SQL语句（INSERT OR REPLACE表示如果存在则更新，否则插入）
      const sql = `
        INSERT OR REPLACE INTO workflows (
          filename, name, folder, workflow_id, active, description, trigger_type,
          complexity, node_count, integrations, tags, created_at, updated_at,
          file_hash, file_size, analyzed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
      `;

      // 准备参数数组
      const params = [
        workflow.filename, // 文件名
        workflow.name, // 工作流名称
        workflow.folder, // 所属文件夹
        workflow.workflow_id, // 工作流ID
        workflow.active, // 是否激活
        workflow.description, // 描述
        workflow.trigger_type, // 触发类型
        workflow.complexity, // 复杂度
        workflow.node_count, // 节点数量
        JSON.stringify(workflow.integrations), // 集成列表（JSON格式）
        JSON.stringify(workflow.tags), // 标签列表（JSON格式）
        workflow.created_at, // 创建时间
        workflow.updated_at, // 更新时间
        workflow.file_hash, // 文件哈希值
        workflow.file_size, // 文件大小
        // analyzed_at 由数据库自动设置为当前时间戳
      ];

      // 执行SQL语句
      this.db.run(sql, params, function (err) {
        if (err) reject(err);
        else resolve(this.lastID); // 返回最后插入的ID
      });
    });
  }

  /**
   * 构建FTS5全文搜索查询语句
   * @param {string} query - 用户输入的搜索查询
   * @returns {string} - 构建好的FTS5查询语句
   */
  buildFTSQuery(query) {
    // 清理查询字符串，移除特殊字符（保留引号、连字符和撇号）
    let cleanQuery = query
      .replace(/[^\w\s"'-]/g, " ") // 移除除字母、数字、空格、引号、连字符和撇号外的所有字符
      .trim();

    // 如果查询为空，返回通配符
    if (!cleanQuery) return "*";

    // 处理带引号的短语（精确匹配）
    const phrases = [];
    const quotedRegex = /"([^"]+)"/g;
    let match;

    while ((match = quotedRegex.exec(cleanQuery)) !== null) {
      phrases.push(`"${match[1]}"`); // 保留精确短语
      cleanQuery = cleanQuery.replace(match[0], " "); // 从查询中移除已处理的短语
    }

    // 处理剩余的搜索词，添加通配符以支持前缀匹配
    const terms = cleanQuery
      .split(/\s+/)
      .filter((term) => term.length > 0)
      .map((term) => {
        // 对于长度大于等于2的词，添加通配符后缀以支持前缀匹配
        if (term.length >= 2) {
          return `${term}*`;
        }
        return term;
      });

    // 合并短语和通配符词
    const allTerms = [...phrases, ...terms];

    // 如果没有有效搜索词，返回通配符
    if (allTerms.length === 0) return "*";

    // 使用AND连接所有词，以获得更精确的结果
    return allTerms.join(" AND ");
  }

  /**
   * 搜索工作流
   * @param {string} query - 搜索查询（支持全文搜索）
   * @param {string} triggerFilter - 触发类型过滤（"all"表示所有类型）
   * @param {string} complexityFilter - 复杂度过滤（"all"表示所有复杂度）
   * @param {boolean} activeOnly - 是否只显示激活的工作流
   * @param {number} limit - 结果数量限制
   * @param {number} offset - 结果偏移量（用于分页）
   * @returns {Promise<Object>} - 搜索结果，包含工作流列表和总数
   */
  async searchWorkflows(
    query = "",
    triggerFilter = "all",
    complexityFilter = "all",
    activeOnly = false,
    limit = 50,
    offset = 0
  ) {
    // 确保数据库已初始化
    if (!this.initialized) {
      await this.initialize();
    }

    return new Promise((resolve, reject) => {
      let sql = "";
      let params = [];

      if (query.trim()) {
        // 使用FTS全文搜索（支持部分匹配）
        const ftsQuery = this.buildFTSQuery(query.trim());
        sql = `
          SELECT w.* FROM workflows w
          JOIN workflows_fts fts ON w.id = fts.rowid
          WHERE workflows_fts MATCH ?
        `;
        params.push(ftsQuery);
      } else {
        // 常规搜索（无全文搜索条件）
        sql = "SELECT * FROM workflows WHERE 1=1";
      }

      // 添加触发类型过滤
      if (triggerFilter !== "all") {
        sql += " AND trigger_type = ?";
        params.push(triggerFilter);
      }

      // 添加复杂度过滤
      if (complexityFilter !== "all") {
        sql += " AND complexity = ?";
        params.push(complexityFilter);
      }

      // 添加激活状态过滤
      if (activeOnly) {
        sql += " AND active = 1";
      }

      // 构建计数查询（用于分页）
      let countSql;
      let countParams = [...params];

      if (query.trim()) {
        // 对于FTS查询，需要重新构建计数查询
        countSql = `
          SELECT COUNT(*) as total FROM workflows w
          JOIN workflows_fts fts ON w.id = fts.rowid
          WHERE workflows_fts MATCH ?
        `;
        countParams = [this.buildFTSQuery(query.trim())];

        // 为计数查询添加相同的过滤条件
        if (triggerFilter !== "all") {
          countSql += " AND trigger_type = ?";
          countParams.push(triggerFilter);
        }

        if (complexityFilter !== "all") {
          countSql += " AND complexity = ?";
          countParams.push(complexityFilter);
        }

        if (activeOnly) {
          countSql += " AND active = 1";
        }
      } else {
        // 对于常规查询，使用子查询计数
        countSql = `SELECT COUNT(*) as total FROM (${sql})`;
        countParams = params.slice(0, -2); // 移除LIMIT和OFFSET参数
      }

      // 执行计数查询
      this.db.get(countSql, countParams, (err, countResult) => {
        if (err) {
          reject(err);
          return;
        }

        const total = countResult.total;

        // 添加分页参数
        sql += " ORDER BY name LIMIT ? OFFSET ?";
        params.push(limit, offset);

        // 执行搜索查询
        this.db.all(sql, params, (err, rows) => {
          if (err) {
            reject(err);
            return;
          }

          // 解析JSON字段
          const workflows = rows.map((row) => ({
            ...row,
            integrations: JSON.parse(row.integrations || "[]"), // 解析集成列表
            tags: JSON.parse(row.tags || "[]"), // 解析标签列表
          }));

          resolve({ workflows, total });
        });
      });
    });
  }

  /**
   * 获取工作流统计信息
   * @returns {Promise<Object>} - 工作流统计信息对象
   */
  async getStats() {
    // 确保数据库已初始化
    if (!this.initialized) {
      await this.initialize();
    }

    return new Promise((resolve, reject) => {
      // 定义统计查询语句
      const queries = [
        "SELECT COUNT(*) as total FROM workflows", // 总工作流数
        "SELECT COUNT(*) as active FROM workflows WHERE active = 1", // 激活的工作流数
        "SELECT COUNT(*) as inactive FROM workflows WHERE active = 0", // 未激活的工作流数
        "SELECT trigger_type, COUNT(*) as count FROM workflows GROUP BY trigger_type", // 按触发类型分组计数
        "SELECT complexity, COUNT(*) as count FROM workflows GROUP BY complexity", // 按复杂度分组计数
        "SELECT SUM(node_count) as total_nodes FROM workflows", // 总节点数
        "SELECT analyzed_at FROM workflows ORDER BY analyzed_at DESC LIMIT 1", // 最后分析时间
      ];

      Promise.all(
        queries.map(
          (sql) =>
            new Promise((resolve, reject) => {
              this.db.all(sql, (err, rows) => {
                if (err) reject(err);
                else resolve(rows);
              });
            })
        )
      )
        .then((results) => {
          const [
            total,
            active,
            inactive,
            triggers,
            complexity,
            nodes,
            lastIndexed,
          ] = results;

          const triggersMap = {};
          triggers.forEach((row) => {
            triggersMap[row.trigger_type] = row.count;
          });

          const complexityMap = {};
          complexity.forEach((row) => {
            complexityMap[row.complexity] = row.count;
          });

          // Count unique integrations
          this.db.all("SELECT integrations FROM workflows", (err, rows) => {
            if (err) {
              reject(err);
              return;
            }

            const allIntegrations = new Set();
            rows.forEach((row) => {
              try {
                const integrations = JSON.parse(row.integrations || "[]");
                integrations.forEach((integration) =>
                  allIntegrations.add(integration)
                );
              } catch (e) {
                // Ignore parse errors
              }
            });

            resolve({
              total: total[0].total,
              active: active[0].active,
              inactive: inactive[0].inactive,
              triggers: triggersMap,
              complexity: complexityMap,
              total_nodes: nodes[0].total_nodes || 0,
              unique_integrations: allIntegrations.size,
              last_indexed: lastIndexed[0]?.analyzed_at || "",
            });
          });
        })
        .catch(reject);
    });
  }

  /**
   * 获取工作流详细信息（包括原始工作流数据）
   * @param {string} filename - 工作流文件名
   * @returns {Promise<Object|null>} - 工作流详细信息对象，如果不存在则返回null
   */
  async getWorkflowDetail(filename) {
    return new Promise((resolve, reject) => {
      this.db.get(
        "SELECT * FROM workflows WHERE filename = ?",
        [filename],
        (err, row) => {
          if (err) {
            reject(err);
            return;
          }

          if (!row) {
            resolve(null);
            return;
          }

          // 解析JSON字段并加载原始工作流数据
          const workflow = {
            ...row,
            integrations: JSON.parse(row.integrations || "[]"), // 解析集成列表
            tags: JSON.parse(row.tags || "[]"), // 解析标签列表
          };

          // 加载原始工作流JSON数据
          try {
            const workflowPath = path.join(this.workflowsDir, filename);
            const rawWorkflow = fs.readJsonSync(workflowPath);
            workflow.raw_workflow = rawWorkflow;
          } catch (error) {
            console.error(
              `加载原始工作流 ${filename} 出错:`,
              error.message
            );
          }

          resolve(workflow);
        }
      );
    });
  }

  /**
   * 关闭数据库连接
   */
  close() {
    if (this.db) {
      this.db.close();
    }
  }
}

module.exports = WorkflowDatabase;
