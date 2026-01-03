/**
 * n8n工作流文档服务器
 * 提供工作流搜索、分析和可视化的RESTful API服务
 * 
 * @module server
 * @requires express
 * @requires cors
 * @requires compression
 * @requires helmet
 * @requires express-rate-limit
 * @requires path
 * @requires fs-extra
 * @requires commander
 * @requires ./database
 */
const express = require('express');
const cors = require('cors');
const compression = require('compression');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const path = require('path');
const fs = require('fs-extra');
const { program } = require('commander');


const WorkflowDatabase = require('./database');

/**
 * 初始化Express应用和数据库连接
 */
const app = express();
const db = new WorkflowDatabase();

/**
 * 安全中间件配置
 * 使用helmet设置HTTP安全头和内容安全策略(CSP)
 */
app.use(helmet({
  contentSecurityPolicy: {
    directives: {
      defaultSrc: ["'self'"], // 默认只允许自身来源
      styleSrc: ["'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"], // 样式来源
      scriptSrc: ["'self'", "'unsafe-inline'", "https://cdn.jsdelivr.net"], // 脚本来源
      imgSrc: ["'self'", "data:", "https:"], // 图片来源
      connectSrc: ["'self'"], // 连接来源
      fontSrc: ["'self'", "https://fonts.gstatic.com"], // 字体来源
      objectSrc: ["'none'"], // 不允许嵌入对象
      mediaSrc: ["'self'"], // 媒体资源来源
      frameSrc: ["'none'"], // 不允许框架
    },
  },
}));

/**
 * 速率限制中间件
 * 限制每个IP在15分钟内最多1000个请求，防止滥用
 */
const limiter = rateLimit({
  windowMs: 15 * 60 * 1000, // 15分钟窗口
  max: 1000, // 每个IP在窗口内的最大请求数
  message: '该IP请求过于频繁，请稍后再试。'
});
app.use('/api/', limiter); // 仅对API路由应用速率限制

/**
 * 通用中间件配置
 */
app.use(compression()); // 启用gzip压缩
app.use(cors()); // 启用跨域资源共享
app.use(express.json()); // 解析JSON请求体
app.use(express.urlencoded({ extended: true })); // 解析URL编码的请求体

/**
 * 静态文件服务
 * 提供static目录下的静态资源
 */
app.use(express.static(path.join(__dirname, '../static')));


/**
 * 健康检查端点
 * 返回服务器运行状态
 */
app.get('/health', (req, res) => {
  res.json({ status: 'healthy', message: 'n8n工作流API正在运行' });
});

/**
 * 主页面端点
 * 提供静态HTML页面，如果不存在则显示设置提示
 */
app.get('/', (req, res) => {
  const staticPath = path.join(__dirname, '../static/index-nodejs.html');
  
  if (fs.existsSync(staticPath)) {
    res.sendFile(staticPath);
  } else {
    res.status(404).send(`
      <html><body>
        <h1>需要设置</h1>
        <p>未找到静态文件。请确保static目录存在并包含index-nodejs.html文件</p>
        <p>当前目录: ${process.cwd()}</p>
      </body></html>
    `);
  }
});

// API路由

/**
 * 获取工作流统计信息
 * 返回工作流总数、平均复杂度等统计数据
 */
app.get('/api/stats', async (req, res) => {
  try {
    const stats = await db.getStats();
    res.json(stats);
  } catch (error) {
    console.error('获取统计信息失败:', error);
    res.status(500).json({ error: '获取统计信息失败', details: error.message });
  }
});


/**
 * 搜索工作流
 * 支持关键词搜索、过滤和分页
 * @param {string} q - 搜索关键词
 * @param {string} trigger - 触发器类型过滤（all表示所有）
 * @param {string} complexity - 复杂度过滤（all表示所有）
 * @param {boolean} active_only - 是否只显示活跃工作流
 * @param {number} page - 当前页码
 * @param {number} per_page - 每页条数
 */
app.get('/api/workflows', async (req, res) => {
  try {
    const {
      q = '',
      trigger = 'all',
      complexity = 'all',
      active_only = false,
      page = 1,
      per_page = 20
    } = req.query;
    
    const pageNum = Math.max(1, parseInt(page));
    const perPage = Math.min(100, Math.max(1, parseInt(per_page)));
    const offset = (pageNum - 1) * perPage;
    const activeOnly = active_only === 'true';
    
    const { workflows, total } = await db.searchWorkflows(
      q, trigger, complexity, activeOnly, perPage, offset
    );
    
    const pages = Math.ceil(total / perPage);
    
    res.json({
      workflows,
      total,
      page: pageNum,
      per_page: perPage,
      pages,
      query: q,
      filters: {
        trigger,
        complexity,
        active_only: activeOnly
      }
    });
  } catch (error) {
    console.error('搜索工作流失败:', error);
    res.status(500).json({ error: '搜索工作流失败', details: error.message });
  }
});

/**
 * 获取工作流详情
 * @param {string} filename - 工作流文件名
 */
app.get('/api/workflows/:filename', async (req, res) => {
  try {
    const { filename } = req.params;
    const workflow = await db.getWorkflowDetail(filename);
    
    if (!workflow) {
      return res.status(404).json({ error: '未找到工作流' });
    }
    
    res.json(workflow);
  } catch (error) {
    console.error('获取工作流详情失败:', error);
    res.status(500).json({ error: '获取工作流详情失败', details: error.message });
  }
});

/**
 * 下载工作流文件
 * @param {string} filename - 工作流文件名
 */
app.get('/api/workflows/:filename/download', async (req, res) => {
  try {
    const { filename } = req.params;
    const workflowPath = path.join('workflows', filename);
    
    if (!fs.existsSync(workflowPath)) {
      return res.status(404).json({ error: '未找到工作流文件' });
    }
    
    res.setHeader('Content-Disposition', `attachment; filename="${filename}"`);
    res.setHeader('Content-Type', 'application/json');
    res.sendFile(path.resolve(workflowPath));
  } catch (error) {
    console.error('下载工作流失败:', error);
    res.status(500).json({ error: '下载工作流失败', details: error.message });
  }
});

/**
 * 获取工作流流程图（Mermaid格式）
 * @param {string} filename - 工作流文件名
 */
app.get('/api/workflows/:filename/diagram', async (req, res) => {
  try {
    const { filename } = req.params;
    const workflow = await db.getWorkflowDetail(filename);
    
    if (!workflow || !workflow.raw_workflow) {
      return res.status(404).json({ error: '未找到工作流' });
    }
    
    const diagram = generateMermaidDiagram(workflow.raw_workflow.nodes, workflow.raw_workflow.connections);
    res.json({ diagram });
  } catch (error) {
    console.error('生成流程图失败:', error);
    res.status(500).json({ error: '生成流程图失败', details: error.message });
  }
});


/**
 * 生成Mermaid流程图
 * 根据工作流节点和连接生成可视化图表
 * @param {Array} nodes - 工作流节点数组
 * @param {Object} connections - 节点间连接关系
 * @returns {string} - Mermaid图表代码
 */
function generateMermaidDiagram(nodes, connections) {
  if (!nodes || nodes.length === 0) {
    return 'graph TD\n    A[未找到节点]';
  }
  
  let diagram = 'graph TD\n';
  
  // 添加节点
  nodes.forEach(node => {
    const nodeId = sanitizeNodeId(node.name);
    const nodeType = node.type?.split('.').pop() || 'unknown';
    diagram += `    ${nodeId}["${node.name}\\n(${nodeType})"]\n`;
  });
  
  // 添加连接关系
  if (connections) {
    Object.entries(connections).forEach(([sourceNode, outputs]) => {
      const sourceId = sanitizeNodeId(sourceNode);
      
      outputs.main?.forEach(outputConnections => {
        outputConnections.forEach(connection => {
          const targetId = sanitizeNodeId(connection.node);
          diagram += `    ${sourceId} --> ${targetId}\n`;
        });
      });
    });
  }
  
  return diagram;
}

/**
 * 清理节点ID
 * 将节点名称转换为有效的Mermaid ID
 * @param {string} nodeName - 原始节点名称
 * @returns {string} - 清理后的节点ID
 */
function sanitizeNodeId(nodeName) {
  // 将节点名称转换为有效的Mermaid ID，只保留字母数字
  return nodeName.replace(/[^a-zA-Z0-9]/g, '_').replace(/^_+|_+$/g, '');
}


/**
 * 重新索引工作流
 * 在后台运行工作流索引更新
 * @param {boolean} force - 是否强制重新索引（忽略已存在的索引）
 */
app.post('/api/reindex', async (req, res) => {
  try {
    const { force = false } = req.body;
    
    // 在后台运行索引更新
    db.indexWorkflows(force).then(results => {
      console.log('索引完成:', results);
    }).catch(error => {
      console.error('索引错误:', error);
    });
    
    res.json({ message: '索引更新已在后台启动' });
  } catch (error) {
    console.error('启动重新索引失败:', error);
    res.status(500).json({ error: '启动重新索引失败', details: error.message });
  }
});

/**
 * 获取所有集成服务
 * 返回工作流中使用的所有第三方集成服务列表
 */
app.get('/api/integrations', async (req, res) => {
  try {
    const { workflows } = await db.searchWorkflows('', 'all', 'all', false, 1000, 0);
    
    const integrations = new Set();
    workflows.forEach(workflow => {
      workflow.integrations.forEach(integration => integrations.add(integration));
    });
    
    res.json(Array.from(integrations).sort());
  } catch (error) {
    console.error('获取集成服务失败:', error);
    res.status(500).json({ error: '获取集成服务失败', details: error.message });
  }
});

/**
 * 获取工作流分类
 * 根据集成服务将工作流分类为不同类别
 */
app.get('/api/categories', async (req, res) => {
  try {
    const { workflows } = await db.searchWorkflows('', 'all', 'all', false, 1000, 0);
    
    const categories = {
      '通信': ['Slack', 'Discord', 'Telegram', 'Mattermost', 'Teams'],
      '客户关系管理': ['HubSpot', 'Salesforce', 'Pipedrive', 'Copper'],
      '数据': ['GoogleSheets', 'Airtable', 'Mysql', 'Postgres'],
      '开发工具': ['GitHub', 'GitLab', 'Jira', 'Trello'],
      '营销': ['Mailchimp', 'Sendinblue', 'Typeform', 'Webflow'],
      '存储': ['GoogleDrive', 'Dropbox', 'OneDrive', 'AWS S3'],
      '其他': []
    };
    
    // 对工作流进行分类
    const categorizedWorkflows = {};
    Object.keys(categories).forEach(category => {
      categorizedWorkflows[category] = [];
    });
    
    workflows.forEach(workflow => {
      let categorized = false;
      
      // 检查每个集成服务是否属于某个分类
      workflow.integrations.forEach(integration => {
        Object.entries(categories).forEach(([category, services]) => {
          if (services.some(service => 
            integration.toLowerCase().includes(service.toLowerCase())
          )) {
            categorizedWorkflows[category].push(workflow);
            categorized = true;
          }
        });
      });
      
      // 如果未分类，则添加到"其他"分类
      if (!categorized) {
        categorizedWorkflows['其他'].push(workflow);
      }
    });
    
    res.json(categorizedWorkflows);
  } catch (error) {
    console.error('获取分类失败:', error);
    res.status(500).json({ error: '获取分类失败', details: error.message });
  }
});

/**
 * 分类映射端点
 * 返回工作流文件名到分类的映射关系
 */
app.get('/api/category-mappings', async (req, res) => {
  try {
    // 获取所有工作流用于构建分类映射
    const { workflows } = await db.searchWorkflows('', 'all', 'all', false, 1000, 0);
    
    // 定义分类规则
    const categories = {
      '通信': ['Slack', 'Discord', 'Telegram', 'Mattermost', 'Teams', 'Email', 'Gmail'],
      '客户关系管理': ['HubSpot', 'Salesforce', 'Pipedrive', 'Copper', 'Zoho'],
      '数据': ['GoogleSheets', 'Airtable', 'Mysql', 'Postgres', 'Mongo', 'Redis', 'Sqlite'],
      '开发工具': ['GitHub', 'GitLab', 'Jira', 'Trello', 'Asana', 'Linear'],
      '营销': ['Mailchimp', 'Sendinblue', 'Typeform', 'Webflow', 'GoogleAnalytics'],
      '存储': ['GoogleDrive', 'Dropbox', 'OneDrive', 'AWS S3', 'Box'],
      '其他': []
    };
    
    // 构建分类映射
    const mappings = {};
    
    workflows.forEach(workflow => {
      let assignedCategory = null;
      
      // 检查每个集成服务是否属于某个分类
      for (const integration of workflow.integrations) {
        for (const [category, services] of Object.entries(categories)) {
          if (category !== '其他' && services.some(service => 
            integration.toLowerCase().includes(service.toLowerCase())
          )) {
            mappings[workflow.filename] = category;
            assignedCategory = category;
            break;
          }
        }
        if (assignedCategory) break;
      }
      
      // 如果未分配分类，则使用"其他"分类
      if (!assignedCategory) {
        mappings[workflow.filename] = '其他';
      }
    });
    
    res.json({ mappings });
  } catch (error) {
    console.error('获取分类映射失败:', error);
    res.status(500).json({ error: '获取分类映射失败', details: error.message });
  }
});

/**
 * 错误处理中间件
 * 捕获并处理所有未处理的错误
 */
app.use((error, req, res, next) => {
  console.error('未处理的错误:', error);
  res.status(500).json({ 
    error: '服务器内部错误', 
    details: process.env.NODE_ENV === 'development' ? error.message : undefined 
  });
});

/**
 * 404处理中间件
 * 处理所有未匹配的路由请求
 */
app.use((req, res) => {
  res.status(404).json({ error: '未找到资源' });
});


/**
 * 启动服务器
 * 初始化Express服务器并监听指定端口
 * @param {number} port - 服务器端口，默认8000
 * @param {string} host - 服务器主机地址，默认127.0.0.1
 */
function startServer(port = 8000, host = '127.0.0.1') {
  const server = app.listen(port, host, () => {
    console.log('🚀 n8n工作流文档服务器');
    console.log('=' .repeat(50));
    console.log(`🌐 服务器运行在 http://${host}:${port}`);
    console.log(`📊 API统计信息: http://${host}:${port}/api/stats`);
    console.log(`🔍 工作流搜索: http://${host}:${port}/api/workflows`);
    console.log();
    console.log('按 Ctrl+C 停止服务器');
    console.log('-'.repeat(50));
  });
  
  // 优雅关闭处理
  process.on('SIGINT', () => {
    console.log('\n👋 正在关闭服务器...');
    server.close(() => {
      db.close();
      console.log('✅ 服务器已停止');
      process.exit(0);
    });
  });
}


/**
 * 命令行界面
 * 当直接运行此文件时，解析命令行参数并启动服务器
 */
if (require.main === module) {
  program
    .option('-p, --port <port>', '服务器运行端口', '8000')
    .option('-h, --host <host>', '服务器绑定地址', '127.0.0.1')
    .option('--dev', '启用开发模式')
    .parse();
  
  const options = program.opts();
  const port = parseInt(options.port);
  const host = options.host;
  
  // 检查数据库是否需要初始化
  db.initialize().then(() => {
    return db.getStats();
  }).then(stats => {
    if (stats.total === 0) {
      console.log('⚠️  警告: 未找到工作流。请运行 "npm run index" 来索引工作流。');
    } else {
      console.log(`✅ 数据库准备就绪: ${stats.total} 个工作流已索引`);
    }
    startServer(port, host);
  }).catch(error => {
    console.error('❌ 数据库连接失败:', error.message);
    process.exit(1);
  });
}


module.exports = app; 