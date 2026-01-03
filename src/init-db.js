#!/usr/bin/env node

const fs = require('fs-extra'); // 文件系统扩展模块
const path = require('path'); // 路径处理模块
const WorkflowDatabase = require('./database'); // 工作流数据库模块

/**
 * 初始化N8N工作流数据库
 * @returns {Promise<void>}
 */
async function initializeDatabase() {
  console.log('🔄 正在初始化N8N工作流数据库...');
  
  try {
    // 确保必要的目录存在
    await fs.ensureDir('database');
    await fs.ensureDir('workflows');
    await fs.ensureDir('static');
    
    console.log('✅ 目录已创建/验证');
    
    // 初始化数据库
    const db = new WorkflowDatabase();
    await db.initialize();
    
    // 获取统计信息以验证数据库正常工作
    const stats = await db.getStats();
    console.log('✅ 数据库初始化成功');
    console.log(`📊 当前统计: ${stats.total} 个工作流`);
    
    db.close();
    
    console.log('\n🎉 初始化完成!');
    console.log('下一步操作:');
    console.log('1. 将您的工作流JSON文件放置在 "workflows" 目录中');
    console.log('2. 运行 "npm run index" 来索引您的工作流');
    console.log('3. 运行 "npm start" 来启动服务器');
    
  } catch (error) {
    console.error('❌ 初始化失败:', error.message);
    process.exit(1);
  }
}

if (require.main === module) {
  initializeDatabase();
}

module.exports = { initializeDatabase }; 