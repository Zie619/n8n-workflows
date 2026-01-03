#!/usr/bin/env node

const { program } = require('commander'); // 命令行解析模块
const WorkflowDatabase = require('./database'); // 工作流数据库模块

/**
 * 打印程序Banner信息
 */
function printBanner() {
  console.log('📚 N8N 工作流索引器');
  console.log('=' .repeat(30));
}

/**
 * 索引所有工作流文件
 * @param {boolean} force - 是否强制重新索引，即使文件哈希未变化
 * @returns {Promise<void>}
 */
async function indexWorkflows(force = false) {
  const db = new WorkflowDatabase();
  
  try {
    console.log('🔄 开始工作流索引...');
    await db.initialize();
    
    const results = await db.indexWorkflows(force);
    
    console.log('✅ 索引完成！');
    console.log(`📊 结果:`);
    console.log(`   • 已处理: ${results.processed}`);
    console.log(`   • 已跳过: ${results.skipped}`);
    console.log(`   • 错误: ${results.errors}`);
    console.log(`   • 总文件数: ${results.total}`);
    
    // 显示最终统计信息
    const stats = await db.getStats();
    console.log(`\n📈 数据库统计:`);
    console.log(`   • 总工作流数: ${stats.total}`);
    console.log(`   • 激活的工作流: ${stats.active}`);
    console.log(`   • 唯一集成数: ${stats.unique_integrations}`);
    console.log(`   • 总节点数: ${stats.total_nodes}`);
    
  } catch (error) {
    console.error('❌ 索引失败:', error.message);
    process.exit(1);
  } finally {
    db.close();
  }
}

// CLI接口配置
program
  .description('将N8N工作流索引到数据库中')
  .option('-f, --force', '强制重新索引所有工作流')
  .option('--stats', '仅显示数据库统计信息')
  .parse();

const options = program.opts();

/**
 * 程序主函数
 */
async function main() {
  printBanner();
  
  const db = new WorkflowDatabase();
  
  if (options.stats) {
    try {
      await db.initialize();
      const stats = await db.getStats();
      console.log('📊 数据库统计信息:');
      console.log(`   • 总工作流数: ${stats.total}`);
      console.log(`   • 激活的工作流: ${stats.active}`);
      console.log(`   • 未激活的工作流: ${stats.inactive}`);
      console.log(`   • 唯一集成数: ${stats.unique_integrations}`);
      console.log(`   • 总节点数: ${stats.total_nodes}`);
      console.log(`   • 最后索引时间: ${stats.last_indexed}`);
      
      if (stats.triggers) {
        console.log(`   • 触发类型:`);
        Object.entries(stats.triggers).forEach(([type, count]) => {
          console.log(`     - ${type}: ${count}`);
        });
      }
      
      if (stats.complexity) {
        console.log(`   • 复杂度分布:`);
        Object.entries(stats.complexity).forEach(([level, count]) => {
          console.log(`     - ${level}: ${count}`);
        });
      }
    } catch (error) {
      console.error('❌ 获取统计信息出错:', error.message);
      process.exit(1);
    } finally {
      db.close();
    }
  } else {
    await indexWorkflows(options.force);
  }
}

if (require.main === module) {
  main();
}

module.exports = { indexWorkflows }; 