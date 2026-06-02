/* CSS Variables for Theming */
:root {
  --primary-color: #ea4b71;
  --primary-dark: #d63859;
  --secondary-color: #6b73ff;
  --accent-color: #00d4aa;
  --text-primary: #2d3748;
  --text-secondary: #4a5568;
  --text-muted: #718096;
  --background: #ffffff;
  --surface: #f7fafc;
  --border: #e2e8f0;
  --border-light: #edf2f7;
  --shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06);
  --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --border-radius: 8px;
  --border-radius-lg: 12px;
  --transition: all 0.2s ease-in-out;
}

/* Dark mode support */
@media (prefers-color-scheme: dark) {
  :root {
    --text-primary: #f7fafc;
    --text-secondary: #e2e8f0;
    --text-muted: #a0aec0;
    --background: #1a202c;
    --surface: #2d3748;
    --border: #4a5568;
    --border-light: #2d3748;
  }
}

/* Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  line-height: 1.6;
  color: var(--text-primary);
  background-color: var(--background);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Header */
.header {
  background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
  color: white;
  padding: 2rem 0;
  text-align: center;
}

.logo {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
}

.logo-emoji {
  font-size: 3rem;
}

.tagline {
  font-size: 1.25rem;
  opacity: 0.9;
  font-weight: 300;
}

/* Search Section */
.search-section {
  padding: 3rem 0;
  background-color: var(--surface);
}

.search-container {
  max-width: 800px;
  margin: 0 auto;
}

.search-box {
  position: relative;
  margin-bottom: 1.5rem;
}

#search-input {
  width: 100%;
  padding: 1rem 3rem 1rem 1.5rem;
  font-size: 1.125rem;
  border: 2px solid var(--border);
  border-radius: var(--border-radius-lg);
  background-color: var(--background);
  color: var(--text-primary);
  transition: var(--transition);
}

#search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(234, 75, 113, 0.1);
}

.search-btn {
  position: absolute;
  right: 0.5rem;
  top: 50%;
  transform: translateY(-50%);
  background: var(--primary-color);
  border: none;
  border-radius: var(--border-radius);
  padding: 0.5rem;
  cursor: pointer;
  transition: var(--transition);
}

.search-btn:hover {
  background: var(--primary-dark);
}

.search-icon {
  font-size: 1.25rem;
}

/* Filters */
.filters {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
}

.filters select {
  padding: 0.75rem 1rem;
  border: 1px solid var(--border);
  border-radius: var(--border-radius);
  background-color: var(--background);
  color: var(--text-primary);
  font-size: 0.875rem;
  cursor: pointer;
}

.filters select:focus {
  outline: none;
  border-color: var(--primary-color);
}

/* Stats Section */
.stats-section {
  padding: 2rem 0;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.stat-card {
  background: var(--background);
  border: 1px solid var(--border);
  border-radius: var(--border-radius-lg);
  padding: 1.5rem;
  text-align: center;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.stat-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 700;
  color: var(--primary-color);
  line-height: 1;
}

.stat-label {
  color: var(--text-muted);
  font-size: 0.875rem;
  font-weight: 500;
  margin-top: 0.5rem;
}

/* Results Section */
.results-section {
  padding: 3rem 0;
}

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.results-header h2 {
  font-size: 1.875rem;
  font-weight: 600;
}

.results-count {
  color: var(--text-muted);
  font-size: 0.875rem;
}

/* Loading State */
.loading {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  padding: 3rem;
  color: var(--text-muted);
}

.spinner {
  width: 24px;
  height: 24px;
  border: 2px solid var(--border);
  border-top: 2px solid var(--primary-color);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

/* Results Grid */
.results-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 1.5rem;
}

/* Workflow Cards */
.workflow-card {
  background: var(--background);
  border: 1px solid var(--border);
  border-radius: var(--border-radius-lg);
  padding: 1.5rem;
  box-shadow: var(--shadow);
  transition: var(--transition);
  cursor: pointer;
}

.workflow-card:hover {
  transform: translateY(-2px);
  box-shadow: var(--shadow-lg);
  border-color: var(--primary-color);
}

.workflow-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
  color: var(--text-primary);
  line-height: 1.4;
}

.workflow-description {
  color: var(--text-secondary);
  font-size: 0.875rem;
  margin-bottom: 1rem;
  line-height: 1.5;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.workflow-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.meta-tag {
  background: var(--surface);
  color: var(--text-muted);
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.meta-tag.category {
  background: var(--accent-color);
  color: white;
}

.meta-tag.trigger {
  background: var(--secondary-color);
  color: white;
}

.workflow-integrations {
  display: flex;
  flex-wrap: wrap;
  gap: 0.25rem;
}

.integration-tag {
  background: var(--primary-color);
  color: white;
  padding: 0.125rem 0.375rem;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.workflow-actions {
  margin-top: 1rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border-light);
  display: flex;
  gap: 0.5rem;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: var(--border-radius);
  font-size: 0.875rem;
  font-weight: 500;
  cursor: pointer;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
  transition: var(--transition);
}

.btn-primary {
  background: var(--primary-color);
  color: white;
}

.btn-primary:hover {
  background: var(--primary-dark);
}

.btn-secondary {
  background: var(--surface);
  color: var(--text-secondary);
  border: 1px solid var(--border);
}

.btn-secondary:hover {
  background: var(--border-light);
}

/* No Results */
.no-results {
  text-align: center;
  padding: 3rem;
  color: var(--text-muted);
}

.no-results-icon {
  font-size: 4rem;
  margin-bottom: 1rem;
}

.no-results h3 {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--text-secondary);
}

/* Load More Button */
.load-more {
  display: block;
  margin: 2rem auto 0;
  padding: 0.75rem 2rem;
  background: var(--primary-color);
  color: white;
  border: none;
  border-radius: var(--border-radius);
  font-size: 1rem;
  font-weight: 500;
  cursor: pointer;
  transition: var(--transition);
}

.load-more:hover {
  background: var(--primary-dark);
}

/* Footer */
.footer {
  background: var(--surface);
  border-top: 1px solid var(--border);
  padding: 2rem 0;
  text-align: center;
  color: var(--text-muted);
  font-size: 0.875rem;
}

.footer-links {
  margin-top: 0.5rem;
}

.footer-links a {
  color: var(--primary-color);
  text-decoration: none;
  margin: 0 0.5rem;
}

.footer-links a:hover {
  text-decoration: underline;
}

/* Utility Classes */
.hidden {
  display: none !important;
}

.text-center {
  text-align: center;
}

/* Responsive Design */
@media (max-width: 768px) {
  .container {
    padding: 0 0.75rem;
  }

  .header {
    padding: 1.5rem 0;
  }

  .logo {
    font-size: 2rem;
  }

  .logo-emoji {
    font-size: 2.5rem;
  }

  .tagline {
    font-size: 1rem;
  }

  .search-section {
    padding: 2rem 0;
  }

  .results-grid {
    grid-template-columns: 1fr;
  }

  .results-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.5rem;
  }

  .filters {
    grid-template-columns: 1fr;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 480px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }

  .workflow-actions {
    flex-direction: column;
  }
}