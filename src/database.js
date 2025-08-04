const sqlite3 = require('sqlite3').verbose();
const path = require('path');
const fs = require('fs-extra');
const crypto = require('crypto');

class WorkflowDatabase {
  constructor(dbPath = 'database/workflows.db') {
    this.dbPath = dbPath;
    this.workflowsDir = 'workflows';
    this.db = null;
    this.initialized = false;
  }

  async initialize() {
    if (this.initialized) return;
    await this.initDatabase();
    this.initialized = true;
  }

  async initDatabase() {
    // Ensure database directory exists
    const dbDir = path.dirname(this.dbPath);
    await fs.ensureDir(dbDir);

    return new Promise((resolve, reject) => {
      this.db = new sqlite3.Database(this.dbPath, (err) => {
        if (err) {
          reject(err);
          return;
        }
        
        // Enable WAL mode for better performance
        this.db.run('PRAGMA journal_mode=WAL');
        this.db.run('PRAGMA synchronous=NORMAL');
        this.db.run('PRAGMA cache_size=10000');
        this.db.run('PRAGMA temp_store=MEMORY');
        
        this.createTables().then(resolve).catch(reject);
      });
    });
  }

  async createTables() {
    // Creating database tables
    return new Promise((resolve, reject) => {
      const queries = [
        // Main workflows table
        `CREATE TABLE IF NOT EXISTS workflows (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          filename TEXT UNIQUE NOT NULL,
          name TEXT NOT NULL,
          workflow_id TEXT,
          active BOOLEAN DEFAULT 0,
          description TEXT,
          translations TEXT,
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
        
        // FTS5 table for full-text search (simplified)
        `CREATE VIRTUAL TABLE IF NOT EXISTS workflows_fts USING fts5(
          filename,
          name,
          description,
          translations,
          integrations,
          tags
        )`,
        
        // Indexes for performance
        'CREATE INDEX IF NOT EXISTS idx_trigger_type ON workflows(trigger_type)',
        'CREATE INDEX IF NOT EXISTS idx_complexity ON workflows(complexity)',
        'CREATE INDEX IF NOT EXISTS idx_active ON workflows(active)',
        'CREATE INDEX IF NOT EXISTS idx_node_count ON workflows(node_count)',
        'CREATE INDEX IF NOT EXISTS idx_filename ON workflows(filename)',
        
        // Triggers to sync FTS table (simplified)
        `CREATE TRIGGER IF NOT EXISTS workflows_ai AFTER INSERT ON workflows BEGIN
          INSERT INTO workflows_fts(filename, name, description, translations, integrations, tags)
          VALUES (new.filename, new.name, new.description, new.translations, new.integrations, new.tags);
        END`,
        
        `CREATE TRIGGER IF NOT EXISTS workflows_ad AFTER DELETE ON workflows BEGIN
          DELETE FROM workflows_fts WHERE filename = old.filename;
        END`,
        
        `CREATE TRIGGER IF NOT EXISTS workflows_au AFTER UPDATE ON workflows BEGIN
          DELETE FROM workflows_fts WHERE filename = old.filename;
          INSERT INTO workflows_fts(filename, name, description, translations, integrations, tags)
          VALUES (new.filename, new.name, new.description, new.translations, new.integrations, new.tags);
        END`
      ];

      // Run queries sequentially to avoid race conditions
      const runQuery = (index) => {
        if (index >= queries.length) {
          resolve();
          return;
        }
        
        const query = queries[index];
        this.db.run(query, (err) => {
          if (err) {
            console.error(`Error in query ${index + 1}:`, err.message);
            reject(err);
            return;
          }
          runQuery(index + 1);
        });
      };
      
      runQuery(0);
    });
  }

  getFileHash(filePath) {
    const buffer = fs.readFileSync(filePath);
    return crypto.createHash('md5').update(buffer).digest('hex');
  }

  formatWorkflowName(filename) {
    // Remove .json extension and split by underscores
    const name = filename.replace('.json', '');
    const parts = name.split('_');
    
    // Skip first part if it's just a number
    const startIndex = parts[0] && /^\d+$/.test(parts[0]) ? 1 : 0;
    const cleanParts = parts.slice(startIndex);
    
    return cleanParts.map(part => {
      const lower = part.toLowerCase();
      const specialTerms = {
        'http': 'HTTP',
        'api': 'API',
        'webhook': 'Webhook',
        'automation': 'Automation',
        'automate': 'Automate',
        'scheduled': 'Scheduled',
        'triggered': 'Triggered',
        'manual': 'Manual'
      };
      
      return specialTerms[lower] || part.charAt(0).toUpperCase() + part.slice(1);
    }).join(' ');
  }

  analyzeWorkflow(filePath) {
    try {
      const data = fs.readJsonSync(filePath);
      const filename = path.basename(filePath);
      const fileSize = fs.statSync(filePath).size;
      const fileHash = this.getFileHash(filePath);
      
      const workflow = {
        filename,
        name: this.formatWorkflowName(filename),
        workflow_id: data.id || '',
        active: data.active || false,
        nodes: data.nodes || [],
        connections: data.connections || {},
        tags: data.tags || [],
        created_at: data.createdAt || '',
        updated_at: data.updatedAt || '',
        file_hash: fileHash,
        file_size: fileSize
      };
      
      // Use meaningful JSON name if available
      const jsonName = data.name?.trim();
      if (jsonName && jsonName !== filename.replace('.json', '') && !jsonName.startsWith('My workflow')) {
        workflow.name = jsonName;
      }
      
      // Analyze nodes
      const nodeCount = workflow.nodes.length;
      workflow.node_count = nodeCount;
      
      // Determine complexity
      if (nodeCount <= 5) {
        workflow.complexity = 'low';
      } else if (nodeCount <= 15) {
        workflow.complexity = 'medium';
      } else {
        workflow.complexity = 'high';
      }
      
      // Analyze trigger type and integrations
      const { triggerType, integrations } = this.analyzeNodes(workflow.nodes);
      workflow.trigger_type = triggerType;
      workflow.integrations = Array.from(integrations);
      
      // Generate description
      workflow.description = data.description || this.generateDescription(workflow, triggerType, integrations);
      workflow.translations = data.translations || {};
      
      return workflow;
    } catch (error) {
      console.error(`Error analyzing workflow ${filePath}:`, error.message);
      return null;
    }
  }

  analyzeNodes(nodes) {
    const integrations = new Set();
    let triggerType = 'Manual';
    
    nodes.forEach(node => {
      const nodeType = node.type || '';
      
      // Extract integration name from node type
      if (nodeType.includes('.')) {
        const parts = nodeType.split('.');
        if (parts.length >= 2) {
          const integration = parts[1];
          if (integration !== 'core' && integration !== 'base') {
            integrations.add(integration.charAt(0).toUpperCase() + integration.slice(1));
          }
        }
      }
      
      // Determine trigger type based on node types
      if (nodeType.includes('webhook')) {
        triggerType = 'Webhook';
      } else if (nodeType.includes('cron') || nodeType.includes('schedule')) {
        triggerType = 'Scheduled';
      } else if (nodeType.includes('trigger')) {
        triggerType = 'Triggered';
      }
    });
    
    return { triggerType, integrations };
  }

  generateDescription(workflow, triggerType, integrations) {
    const parts = [];
    
    // Add trigger info
    if (triggerType !== 'Manual') {
      parts.push(`${triggerType} workflow`);
    } else {
      parts.push('Manual workflow');
    }
    
    // Add integration info
    if (integrations.size > 0) {
      const integrationList = Array.from(integrations).slice(0, 3);
      if (integrations.size > 3) {
        integrationList.push(`+${integrations.size - 3} more`);
      }
      parts.push(`integrating ${integrationList.join(', ')}`);
    }
    
    // Add complexity info
    parts.push(`with ${workflow.node_count} nodes (${workflow.complexity} complexity)`);
    
    return parts.join(' ');
  }

  async indexWorkflows(forceReindex = false) {
    if (!this.initialized) {
      await this.initialize();
    }
    
    const workflowFiles = await fs.readdir(this.workflowsDir);
    const jsonFiles = workflowFiles.filter(file => file.endsWith('.json'));
    
    let processed = 0;
    let skipped = 0;
    let errors = 0;
    
    for (const file of jsonFiles) {
      const filePath = path.join(this.workflowsDir, file);
      const workflow = this.analyzeWorkflow(filePath);
      
      if (!workflow) {
        errors++;
        continue;
      }
      
      try {
        // Check if workflow exists and if hash changed
        const existing = await this.getWorkflowByFilename(file);
        if (!forceReindex && existing && existing.file_hash === workflow.file_hash) {
          skipped++;
          continue;
        }
        
        await this.upsertWorkflow(workflow);
        processed++;
      } catch (error) {
        console.error(`Error indexing workflow ${file}:`, error.message);
        errors++;
      }
    }
    
    return { processed, skipped, errors, total: jsonFiles.length };
  }

  async getWorkflowByFilename(filename) {
    return new Promise((resolve, reject) => {
      this.db.get(
        'SELECT * FROM workflows WHERE filename = ?',
        [filename],
        (err, row) => {
          if (err) reject(err);
          else resolve(row);
        }
      );
    });
  }

  async upsertWorkflow(workflow) {
    return new Promise((resolve, reject) => {
      const sql = `
        INSERT OR REPLACE INTO workflows (
          filename, name, workflow_id, active, description, translations, trigger_type,
          complexity, node_count, integrations, tags, created_at, updated_at,
          file_hash, file_size, analyzed_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
      `;
      
      const params = [
        workflow.filename,
        workflow.name,
        workflow.workflow_id,
        workflow.active,
        workflow.description,
        JSON.stringify(workflow.translations),
        workflow.trigger_type,
        workflow.complexity,
        workflow.node_count,
        JSON.stringify(workflow.integrations),
        JSON.stringify(workflow.tags),
        workflow.created_at,
        workflow.updated_at,
        workflow.file_hash,
        workflow.file_size
      ];
      
      this.db.run(sql, params, function(err) {
        if (err) reject(err);
        else resolve(this.lastID);
      });
    });
  }

  buildFTSQuery(query) {
    // Escape FTS5 special characters and build partial matching query
    let cleanQuery = query
      .replace(/[^\w\s"'-]/g, ' ') // Remove special chars except quotes, hyphens, apostrophes
      .trim();
    
    if (!cleanQuery) return '*';
    
    // Handle quoted phrases
    const phrases = [];
    const quotedRegex = /"([^"]+)"/g;
    let match;
    
    while ((match = quotedRegex.exec(cleanQuery)) !== null) {
      phrases.push(`"${match[1]}"`); // Keep exact phrases
      cleanQuery = cleanQuery.replace(match[0], ' ');
    }
    
    // Split remaining terms and add wildcards for partial matching
    const terms = cleanQuery
      .split(/\s+/)
      .filter(term => term.length > 0)
      .map(term => {
        // Add wildcard suffix for prefix matching
        if (term.length >= 2) {
          return `${term}*`;
        }
        return term;
      });
    
    // Combine phrases and wildcard terms
    const allTerms = [...phrases, ...terms];
    
    if (allTerms.length === 0) return '*';
    
    // Join with AND for more precise results
    return allTerms.join(' AND ');
  }

  async searchWorkflows(query = '', triggerFilter = 'all', complexityFilter = 'all', 
                       activeOnly = false, limit = 50, offset = 0) {
    if (!this.initialized) {
      await this.initialize();
    }
    
    return new Promise((resolve, reject) => {
      let sql = '';
      let params = [];
      
      if (query.trim()) {
        // Use FTS search with partial matching
        const ftsQuery = this.buildFTSQuery(query.trim());
        sql = `
          SELECT w.* FROM workflows w
          JOIN workflows_fts fts ON w.id = fts.rowid
          WHERE workflows_fts MATCH ?
        `;
        params.push(ftsQuery);
      } else {
        // Regular search
        sql = 'SELECT * FROM workflows WHERE 1=1';
      }
      
      // Add filters
      if (triggerFilter !== 'all') {
        sql += ' AND trigger_type = ?';
        params.push(triggerFilter);
      }
      
      if (complexityFilter !== 'all') {
        sql += ' AND complexity = ?';
        params.push(complexityFilter);
      }
      
      if (activeOnly) {
        sql += ' AND active = 1';
      }
      
      // Count total - rebuild query for FTS compatibility
      let countSql;
      let countParams = [...params];
      
      if (query.trim()) {
        // For FTS queries, we need to rebuild the count query
        countSql = `
          SELECT COUNT(*) as total FROM workflows w
          JOIN workflows_fts fts ON w.id = fts.rowid
          WHERE workflows_fts MATCH ?
        `;
        countParams = [this.buildFTSQuery(query.trim())];
        
        // Add filters to count query
        if (triggerFilter !== 'all') {
          countSql += ' AND trigger_type = ?';
          countParams.push(triggerFilter);
        }
        
        if (complexityFilter !== 'all') {
          countSql += ' AND complexity = ?';
          countParams.push(complexityFilter);
        }
        
        if (activeOnly) {
          countSql += ' AND active = 1';
        }
      } else {
        countSql = `SELECT COUNT(*) as total FROM (${sql})`;
        countParams = params.slice(0, -2); // Remove LIMIT and OFFSET for count
      }
      
      this.db.get(countSql, countParams, (err, countResult) => {
        if (err) {
          reject(err);
          return;
        }
        
        const total = countResult.total;
        
        // Add pagination
        sql += ' ORDER BY name LIMIT ? OFFSET ?';
        params.push(limit, offset);
        
        this.db.all(sql, params, (err, rows) => {
          if (err) {
            reject(err);
            return;
          }
          
          // Parse JSON fields
          const workflows = rows.map(row => ({
            ...row,
            integrations: JSON.parse(row.integrations || '[]'),
            tags: JSON.parse(row.tags || '[]'),
            translations: JSON.parse(row.translations || '{}')
          }));
          
          resolve({ workflows, total });
        });
      });
    });
  }

  async getStats() {
    if (!this.initialized) {
      await this.initialize();
    }
    
    return new Promise((resolve, reject) => {
      const queries = [
        'SELECT COUNT(*) as total FROM workflows',
        'SELECT COUNT(*) as active FROM workflows WHERE active = 1',
        'SELECT COUNT(*) as inactive FROM workflows WHERE active = 0',
        'SELECT trigger_type, COUNT(*) as count FROM workflows GROUP BY trigger_type',
        'SELECT complexity, COUNT(*) as count FROM workflows GROUP BY complexity',
        'SELECT SUM(node_count) as total_nodes FROM workflows',
        'SELECT analyzed_at FROM workflows ORDER BY analyzed_at DESC LIMIT 1'
      ];
      
      Promise.all(queries.map(sql => 
        new Promise((resolve, reject) => {
          this.db.all(sql, (err, rows) => {
            if (err) reject(err);
            else resolve(rows);
          });
        })
      )).then(results => {
        const [total, active, inactive, triggers, complexity, nodes, lastIndexed] = results;
        
        const triggersMap = {};
        triggers.forEach(row => {
          triggersMap[row.trigger_type] = row.count;
        });
        
        const complexityMap = {};
        complexity.forEach(row => {
          complexityMap[row.complexity] = row.count;
        });
        
        // Count unique integrations
        this.db.all('SELECT integrations FROM workflows', (err, rows) => {
          if (err) {
            reject(err);
            return;
          }
          
          const allIntegrations = new Set();
          rows.forEach(row => {
            try {
              const integrations = JSON.parse(row.integrations || '[]');
              integrations.forEach(integration => allIntegrations.add(integration));
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
            last_indexed: lastIndexed[0]?.analyzed_at || ''
          });
        });
      }).catch(reject);
    });
  }

  async getWorkflowDetail(filename) {
    return new Promise((resolve, reject) => {
      this.db.get(
        'SELECT * FROM workflows WHERE filename = ?',
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
          
          // Parse JSON fields and load raw workflow data
          const workflow = {
            ...row,
            integrations: JSON.parse(row.integrations || '[]'),
            tags: JSON.parse(row.tags || '[]'),
            translations: JSON.parse(row.translations || '{}')
          };
          
          // Load raw workflow JSON
          try {
            const workflowPath = path.join(this.workflowsDir, filename);
            const rawWorkflow = fs.readJsonSync(workflowPath);
            workflow.raw_workflow = rawWorkflow;
          } catch (error) {
            console.error(`Error loading raw workflow ${filename}:`, error.message);
          }
          
          resolve(workflow);
        }
      );
    });
  }

  close() {
    if (this.db) {
      this.db.close();
    }
  }
}

module.exports = WorkflowDatabase; 