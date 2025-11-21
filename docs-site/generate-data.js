#!/usr/bin/env node

/**
 * Script to generate data.json from workflow files
 * Run this script before deploying to Netlify:
 *   node generate-data.js
 */

const fs = require('fs');
const path = require('path');

const WORKFLOWS_DIR = path.join(__dirname, '../workflows');
const OUTPUT_FILE = path.join(__dirname, 'data.json');

function getAllJsonFiles(dir, fileList = []) {
    const files = fs.readdirSync(dir);

    files.forEach(file => {
        const filePath = path.join(dir, file);
        const stat = fs.statSync(filePath);

        if (stat.isDirectory()) {
            // Recursively search in subdirectories
            getAllJsonFiles(filePath, fileList);
        } else if (file.endsWith('.json')) {
            fileList.push(filePath);
        }
    });

    return fileList;
}

function generateDataFile() {
    console.log('🔍 Scanning workflows directory recursively...');

    // Check if workflows directory exists
    if (!fs.existsSync(WORKFLOWS_DIR)) {
        console.error('❌ Error: workflows directory not found at:', WORKFLOWS_DIR);
        process.exit(1);
    }

    // Get all JSON files recursively
    const files = getAllJsonFiles(WORKFLOWS_DIR);

    console.log(`📄 Found ${files.length} workflow file(s)`);

    // Load all workflows
    const workflows = [];
    files.forEach(filePath => {
        try {
            const content = fs.readFileSync(filePath, 'utf8');
            const workflow = JSON.parse(content);
            workflows.push(workflow);
            const relativePath = path.relative(WORKFLOWS_DIR, filePath);
            console.log(`  ✓ Loaded: ${relativePath}`);
        } catch (error) {
            const relativePath = path.relative(WORKFLOWS_DIR, filePath);
            console.error(`  ✗ Error loading ${relativePath}:`, error.message);
        }
    });

    // Create data object
    const data = {
        generated: new Date().toISOString(),
        count: workflows.length,
        workflows: workflows
    };

    // Write to output file
    fs.writeFileSync(OUTPUT_FILE, JSON.stringify(data, null, 2));

    console.log(`\n✅ Successfully generated data.json with ${workflows.length} workflow(s)`);
    console.log(`📍 Output file: ${OUTPUT_FILE}`);

    // Display summary statistics
    const totalNodes = workflows.reduce((sum, w) => sum + (w.nodes?.length || 0), 0);
    const nodeTypes = new Set();
    workflows.forEach(w => {
        (w.nodes || []).forEach(n => nodeTypes.add(n.type));
    });

    console.log('\n📊 Statistics:');
    console.log(`   - Total workflows: ${workflows.length}`);
    console.log(`   - Total nodes: ${totalNodes}`);
    console.log(`   - Unique node types: ${nodeTypes.size}`);
}

// Run the generator
try {
    generateDataFile();
} catch (error) {
    console.error('❌ Error:', error.message);
    process.exit(1);
}
