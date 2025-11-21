// Main Application Logic
class WorkflowDocumentation {
    constructor() {
        this.workflows = [];
        this.init();
    }

    async init() {
        try {
            await this.loadWorkflows();
            this.setupEventListeners();
            this.renderOverview();
            this.renderWorkflows();
            this.renderNodesCatalog();
            this.renderStatistics();
            this.hideLoading();
        } catch (error) {
            this.showError(error.message);
        }
    }

    async loadWorkflows() {
        try {
            // Try to load from generated data file
            const response = await fetch('data.json');
            if (!response.ok) {
                throw new Error('Impossible de charger les workflows. Assurez-vous que data.json existe.');
            }
            const data = await response.json();
            this.workflows = data.workflows || [];
        } catch (error) {
            // If data.json doesn't exist, try to load from GitHub API
            console.warn('data.json not found, attempting to load from GitHub...');
            await this.loadFromGitHub();
        }
    }

    async loadFromGitHub() {
        try {
            const owner = 'Willer258';
            const repo = 'n8n-workflows';
            const path = 'workflows';

            // Get list of workflow files
            const response = await fetch(`https://api.github.com/repos/${owner}/${repo}/contents/${path}`);
            if (!response.ok) throw new Error('Impossible de charger depuis GitHub');

            const files = await response.json();
            const jsonFiles = files.filter(file => file.name.endsWith('.json'));

            // Load each workflow file
            const workflowPromises = jsonFiles.map(async file => {
                const fileResponse = await fetch(file.download_url);
                const workflow = await fileResponse.json();
                return workflow;
            });

            this.workflows = await Promise.all(workflowPromises);
        } catch (error) {
            throw new Error('Impossible de charger les workflows. Veuillez générer le fichier data.json.');
        }
    }

    setupEventListeners() {
        // Tab switching
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                const tab = btn.dataset.tab;
                this.switchTab(tab);
            });
        });

        // Workflow search
        const workflowSearch = document.getElementById('workflow-search');
        if (workflowSearch) {
            workflowSearch.addEventListener('input', (e) => {
                this.filterWorkflows(e.target.value);
            });
        }

        // Node search
        const nodeSearch = document.getElementById('node-search');
        if (nodeSearch) {
            nodeSearch.addEventListener('input', (e) => {
                this.filterNodes(e.target.value);
            });
        }
    }

    switchTab(tabName) {
        // Update tab buttons
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

        // Update tab content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });
        document.getElementById(tabName).classList.add('active');
    }

    renderOverview() {
        const stats = this.calculateStats();
        const statsContainer = document.getElementById('overview-stats');

        statsContainer.innerHTML = `
            <div class="stat-card">
                <div class="stat-icon">📊</div>
                <span class="stat-value">${stats.totalWorkflows}</span>
                <div class="stat-label">Workflows Totaux</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🔧</div>
                <span class="stat-value">${stats.totalNodes}</span>
                <div class="stat-label">Nodes Totaux</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🎯</div>
                <span class="stat-value">${stats.uniqueNodeTypes}</span>
                <div class="stat-label">Types de Nodes</div>
            </div>
            <div class="stat-card">
                <div class="stat-icon">🔗</div>
                <span class="stat-value">${stats.totalConnections}</span>
                <div class="stat-label">Connexions</div>
            </div>
        `;
    }

    renderWorkflows() {
        const workflowsList = document.getElementById('workflows-list');

        if (this.workflows.length === 0) {
            workflowsList.innerHTML = `
                <div class="card text-center">
                    <p>Aucun workflow trouvé. Assurez-vous que les fichiers workflow sont présents.</p>
                </div>
            `;
            return;
        }

        workflowsList.innerHTML = this.workflows.map(workflow => {
            const nodes = workflow.nodes || [];
            const connections = workflow.connections || {};
            const tags = workflow.tags || [];
            const created = workflow.createdAt ? new Date(workflow.createdAt).toLocaleDateString('fr-FR') : 'N/A';
            const updated = workflow.updatedAt ? new Date(workflow.updatedAt).toLocaleDateString('fr-FR') : 'N/A';

            // Get unique node types
            const nodeTypes = [...new Set(nodes.map(n => n.type))];

            // Count connections
            const connectionCount = Object.values(connections).reduce((total, conn) => {
                return total + Object.values(conn).reduce((sum, arr) => sum + arr.length, 0);
            }, 0);

            return `
                <div class="workflow-card" data-workflow-name="${workflow.name?.toLowerCase() || ''}">
                    <div class="workflow-header">
                        <div>
                            <h3 class="workflow-title">${this.escapeHtml(workflow.name || 'Sans nom')}</h3>
                            <div class="workflow-meta">
                                <span class="meta-item">
                                    <span>📅</span>
                                    Créé: ${created}
                                </span>
                                <span class="meta-item">
                                    <span>🔄</span>
                                    Mis à jour: ${updated}
                                </span>
                            </div>
                        </div>
                    </div>

                    ${tags.length > 0 ? `
                        <div class="workflow-tags">
                            ${tags.map(tag => `<span class="tag">${this.escapeHtml(tag.name || tag)}</span>`).join('')}
                        </div>
                    ` : ''}

                    <div class="workflow-meta">
                        <span class="meta-item">
                            <span>🔧</span>
                            ${nodes.length} node${nodes.length > 1 ? 's' : ''}
                        </span>
                        <span class="meta-item">
                            <span>🔗</span>
                            ${connectionCount} connexion${connectionCount > 1 ? 's' : ''}
                        </span>
                        <span class="meta-item">
                            <span>🎯</span>
                            ${nodeTypes.length} type${nodeTypes.length > 1 ? 's' : ''}
                        </span>
                    </div>

                    ${nodes.length > 0 ? `
                        <div class="workflow-nodes">
                            <strong style="color: var(--text-secondary); font-size: 0.9rem;">Nodes utilisés:</strong>
                            <div class="nodes-list">
                                ${nodeTypes.slice(0, 10).map(type => `
                                    <span class="node-badge">${this.escapeHtml(type)}</span>
                                `).join('')}
                                ${nodeTypes.length > 10 ? `<span class="node-badge">+${nodeTypes.length - 10} autres</span>` : ''}
                            </div>
                        </div>
                    ` : ''}
                </div>
            `;
        }).join('');
    }

    renderNodesCatalog() {
        const nodesCatalog = document.getElementById('nodes-catalog');
        const nodeStats = this.getNodeStatistics();

        if (nodeStats.length === 0) {
            nodesCatalog.innerHTML = `
                <div class="card text-center">
                    <p>Aucun node trouvé.</p>
                </div>
            `;
            return;
        }

        nodesCatalog.innerHTML = nodeStats.map(node => `
            <div class="node-catalog-card" data-node-type="${node.type.toLowerCase()}">
                <div class="node-catalog-header">
                    <h3 class="node-catalog-name">${this.escapeHtml(node.type)}</h3>
                    <span class="node-count">${node.count}</span>
                </div>
                <div class="workflows-using">
                    Utilisé dans <strong>${node.workflows.size}</strong> workflow${node.workflows.size > 1 ? 's' : ''}
                </div>
            </div>
        `).join('');
    }

    renderStatistics() {
        const statistics = document.getElementById('statistics');
        const stats = this.calculateDetailedStats();

        statistics.innerHTML = `
            <div class="stat-section">
                <h3>📊 Statistiques Globales</h3>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon">📁</div>
                        <span class="stat-value">${stats.totalWorkflows}</span>
                        <div class="stat-label">Workflows Totaux</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">🔧</div>
                        <span class="stat-value">${stats.totalNodes}</span>
                        <div class="stat-label">Nodes Totaux</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">📊</div>
                        <span class="stat-value">${stats.avgNodesPerWorkflow.toFixed(1)}</span>
                        <div class="stat-label">Nodes Moyens/Workflow</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">🔗</div>
                        <span class="stat-value">${stats.totalConnections}</span>
                        <div class="stat-label">Connexions Totales</div>
                    </div>
                </div>
            </div>

            <div class="stat-section">
                <h3>🏆 Top 10 Nodes les Plus Utilisés</h3>
                <div class="node-types">
                    ${stats.topNodes.slice(0, 10).map(node => `
                        <div class="node-type-item">
                            <strong>${this.escapeHtml(node.type)}</strong>
                            <span>${node.count} utilisations dans ${node.workflows.size} workflow${node.workflows.size > 1 ? 's' : ''}</span>
                        </div>
                    `).join('')}
                </div>
            </div>

            ${stats.workflowsByTag.length > 0 ? `
                <div class="stat-section">
                    <h3>🏷️ Workflows par Tag</h3>
                    <div class="node-types">
                        ${stats.workflowsByTag.map(tag => `
                            <div class="node-type-item">
                                <strong>${this.escapeHtml(tag.tag)}</strong>
                                <span>${tag.count} workflow${tag.count > 1 ? 's' : ''}</span>
                            </div>
                        `).join('')}
                    </div>
                </div>
            ` : ''}

            <div class="stat-section">
                <h3>📈 Complexité des Workflows</h3>
                <div class="stats-grid">
                    <div class="stat-card">
                        <div class="stat-icon">🎯</div>
                        <span class="stat-value">${stats.simpleWorkflows}</span>
                        <div class="stat-label">Workflows Simples (1-5 nodes)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">⚙️</div>
                        <span class="stat-value">${stats.mediumWorkflows}</span>
                        <div class="stat-label">Workflows Moyens (6-15 nodes)</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-icon">🚀</div>
                        <span class="stat-value">${stats.complexWorkflows}</span>
                        <div class="stat-label">Workflows Complexes (16+ nodes)</div>
                    </div>
                </div>
            </div>
        `;
    }

    calculateStats() {
        const totalWorkflows = this.workflows.length;
        const totalNodes = this.workflows.reduce((sum, w) => sum + (w.nodes?.length || 0), 0);
        const allNodeTypes = new Set();
        let totalConnections = 0;

        this.workflows.forEach(workflow => {
            (workflow.nodes || []).forEach(node => {
                allNodeTypes.add(node.type);
            });

            const connections = workflow.connections || {};
            totalConnections += Object.values(connections).reduce((total, conn) => {
                return total + Object.values(conn).reduce((sum, arr) => sum + arr.length, 0);
            }, 0);
        });

        return {
            totalWorkflows,
            totalNodes,
            uniqueNodeTypes: allNodeTypes.size,
            totalConnections
        };
    }

    calculateDetailedStats() {
        const stats = this.calculateStats();
        const nodeStats = this.getNodeStatistics();

        // Calculate workflow complexity
        let simpleWorkflows = 0;
        let mediumWorkflows = 0;
        let complexWorkflows = 0;

        this.workflows.forEach(workflow => {
            const nodeCount = workflow.nodes?.length || 0;
            if (nodeCount <= 5) simpleWorkflows++;
            else if (nodeCount <= 15) mediumWorkflows++;
            else complexWorkflows++;
        });

        // Get tags statistics
        const tagMap = new Map();
        this.workflows.forEach(workflow => {
            (workflow.tags || []).forEach(tag => {
                const tagName = tag.name || tag;
                tagMap.set(tagName, (tagMap.get(tagName) || 0) + 1);
            });
        });

        const workflowsByTag = Array.from(tagMap.entries())
            .map(([tag, count]) => ({ tag, count }))
            .sort((a, b) => b.count - a.count);

        return {
            ...stats,
            avgNodesPerWorkflow: stats.totalNodes / stats.totalWorkflows || 0,
            topNodes: nodeStats,
            simpleWorkflows,
            mediumWorkflows,
            complexWorkflows,
            workflowsByTag
        };
    }

    getNodeStatistics() {
        const nodeMap = new Map();

        this.workflows.forEach(workflow => {
            const workflowName = workflow.name || 'Sans nom';
            (workflow.nodes || []).forEach(node => {
                if (!nodeMap.has(node.type)) {
                    nodeMap.set(node.type, {
                        type: node.type,
                        count: 0,
                        workflows: new Set()
                    });
                }
                const stat = nodeMap.get(node.type);
                stat.count++;
                stat.workflows.add(workflowName);
            });
        });

        return Array.from(nodeMap.values())
            .sort((a, b) => b.count - a.count);
    }

    filterWorkflows(searchTerm) {
        const term = searchTerm.toLowerCase();
        const workflowCards = document.querySelectorAll('.workflow-card');

        workflowCards.forEach(card => {
            const workflowName = card.dataset.workflowName;
            const shouldShow = workflowName.includes(term);
            card.style.display = shouldShow ? '' : 'none';
        });
    }

    filterNodes(searchTerm) {
        const term = searchTerm.toLowerCase();
        const nodeCards = document.querySelectorAll('.node-catalog-card');

        nodeCards.forEach(card => {
            const nodeType = card.dataset.nodeType;
            const shouldShow = nodeType.includes(term);
            card.style.display = shouldShow ? '' : 'none';
        });
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    hideLoading() {
        document.getElementById('loading').classList.add('hidden');
    }

    showError(message) {
        document.getElementById('loading').classList.add('hidden');
        document.getElementById('error').classList.remove('hidden');
        document.getElementById('error-message').textContent = message;
    }
}

// Initialize the application when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new WorkflowDocumentation();
});
