/**
 * Main application script for N8N Workflow Collection
 * Handles additional UI interactions and utilities
 */

class WorkflowApp {
    constructor() {
        this.init();
    }

    init() {
        this.setupThemeToggle();
        this.setupKeyboardShortcuts();
        this.setupAnalytics();
        this.setupServiceWorker();
    }

    setupThemeToggle() {
        // Add theme toggle functionality if needed
        const prefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
        if (prefersDark) {
            document.documentElement.classList.add('dark-theme');
        }
    }

    setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Focus search on '/' key
            if (e.key === '/' && !e.ctrlKey && !e.metaKey && !e.altKey) {
                e.preventDefault();
                const searchInput = document.getElementById('search-input');
                if (searchInput) {
                    searchInput.focus();
                }
            }

            // Clear search on 'Escape' key
            if (e.key === 'Escape') {
                const searchInput = document.getElementById('search-input');
                if (searchInput && searchInput.value) {
                    searchInput.value = '';
                    searchInput.dispatchEvent(new Event('input'));
                }
            }
        });
    }

    setupAnalytics() {
        // Basic analytics for tracking popular workflows
        this.trackEvent = (category, action, label) => {
            // Could integrate with Google Analytics or other tracking
            console.debug('Analytics:', { category, action, label });
        };

        // Track search queries
        const searchInput = document.getElementById('search-input');
        if (searchInput) {
            searchInput.addEventListener('input', this.debounce((e) => {
                if (e.target.value.length > 2) {
                    this.trackEvent('Search', 'query', e.target.value);
                }
            }, 1000));
        }

        // Track workflow downloads
        document.addEventListener('click', (e) => {
            if (e.target.matches('a[href*=".json"]')) {
                const filename = e.target.href.split('/').pop();
                this.trackEvent('Download', 'workflow', filename);
            }
        });
    }

    setupServiceWorker() {
        // Register service worker for offline functionality (if needed)
        if ('serviceWorker' in navigator) {
            // Uncomment when service worker is implemented
            // navigator.serviceWorker.register('/service-worker.js');
        }
    }

    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }
}

// Utility functions for the application
window.WorkflowUtils = {
    /**
     * Format numbers with appropriate suffixes
     */
    formatNumber(num) {
        if (num >= 1000000) {
            return (num / 1000000).toFixed(1) + 'M';
        }
        if (num >= 1000) {
            return (num / 1000).toFixed(1) + 'K';
        }
        return num.toString();
    },

    /**
     * Debounce function for search input
     */
    debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    },

    /**
     * Copy text to clipboard
     */
    async copyToClipboard(text) {
        try {
            await navigator.clipboard.writeText(text);
            return true;
        } catch (err) {
            // Fallback for older browsers
            const textArea = document.createElement('textarea');
            textArea.value = text;
            document.body.appendChild(textArea);
            textArea.select();
            const success = document.execCommand('copy');
            document.body.removeChild(textArea);
            return success;
        }
    },

    /**
     * Show temporary notification
     */
    showNotification(message, type = 'info', duration = 3000) {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            background: ${type === 'success' ? '#48bb78' : type === 'error' ? '#f56565' : '#4299e1'};
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            z-index: 1000;
            opacity: 0;
            transform: translateX(100%);
            transition: all 0.3s ease;
        `;
        notification.textContent = message;

        document.body.appendChild(notification);

        // Animate in
        setTimeout(() => {
            notification.style.opacity = '1';
            notification.style.transform = 'translateX(0)';
        }, 10);

        // Animate out and remove
        setTimeout(() => {
            notification.style.opacity = '0';
            notification.style.transform = 'translateX(100%)';
            setTimeout(() => {
                if (notification.parentNode) {
                    document.body.removeChild(notification);
                }
            }, 300);
        }, duration);
    }
};

// Initialize app when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    new WorkflowApp();

    // Add helpful hints
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.setAttribute('title', 'Press / to focus search, Escape to clear');
    }
});

// Handle page visibility changes
document.addEventListener('visibilitychange', () => {
    if (document.visibilityState === 'visible') {
        // Refresh data if page has been hidden for more than 5 minutes
        const lastRefresh = localStorage.getItem('lastRefresh');
        const now = Date.now();
        if (!lastRefresh || now - parseInt(lastRefresh) > 5 * 60 * 1000) {
            // Could refresh search index here if needed
            localStorage.setItem('lastRefresh', now.toString());
        }
    }
});