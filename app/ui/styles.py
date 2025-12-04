"""
Global CSS styling for Stock Analyzer - Modern & Clean Design
"""

GLOBAL_CSS = """
:root {
    --color-primary: #0066CC;
    --color-primary-dark: #0052A3;
    --color-primary-light: #E6F0FF;
    --color-secondary: #6C757D;
    --color-success: #28A745;
    --color-danger: #DC3545;
    --color-warning: #FFC107;
    --color-info: #17A2B8;
    --color-light: #F8F9FA;
    --color-dark: #212529;
    --color-gray: #6C757D;
    --color-border: #E9ECEF;
    
    --spacing-xs: 0.25rem;
    --spacing-sm: 0.5rem;
    --spacing-md: 1rem;
    --spacing-lg: 1.5rem;
    --spacing-xl: 2rem;
    --spacing-2xl: 3rem;
    
    --border-radius-sm: 0.25rem;
    --border-radius-md: 0.5rem;
    --border-radius-lg: 0.75rem;
    --border-radius-xl: 1rem;
    
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);
    
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
    background: linear-gradient(135deg, #F5F7FA 0%, #C3CFE2 100%);
    color: var(--color-dark);
    line-height: 1.6;
    min-height: 100vh;
    padding-top: 70px;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    color: var(--color-dark);
    font-weight: 700;
    margin-bottom: var(--spacing-md);
    letter-spacing: -0.01em;
}

h1 { font-size: 2.5rem; font-weight: 800; }
h2 { font-size: 2rem; }
h3 { font-size: 1.5rem; }
h4 { font-size: 1.25rem; }
h5 { font-size: 1.125rem; }
h6 { font-size: 1rem; }

p {
    margin-bottom: var(--spacing-md);
    color: var(--color-gray);
    font-size: 0.95rem;
    line-height: 1.7;
}

small {
    font-size: 0.85rem;
    color: var(--color-gray);
}

/* Links */
a {
    color: var(--color-primary);
    text-decoration: none;
    transition: color var(--transition-fast);
    font-weight: 500;
}

a:hover {
    color: var(--color-primary-dark);
    text-decoration: underline;
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.65rem 1.25rem;
    border-radius: var(--border-radius-md);
    font-weight: 600;
    border: none;
    cursor: pointer;
    transition: all var(--transition-base);
    font-size: 0.95rem;
    gap: 0.5rem;
    white-space: nowrap;
}

.btn:active {
    transform: scale(0.98);
}

.btn-primary {
    background: linear-gradient(135deg, var(--color-primary) 0%, var(--color-primary-dark) 100%);
    color: white;
    box-shadow: var(--shadow-md);
}

.btn-primary:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: var(--color-light);
    color: var(--color-dark);
    border: 1px solid var(--color-border);
}

.btn-secondary:hover {
    background-color: #E9ECEF;
    border-color: #DDD;
}

.btn-success {
    background-color: var(--color-success);
    color: white;
    box-shadow: var(--shadow-md);
}

.btn-danger {
    background-color: var(--color-danger);
    color: white;
    box-shadow: var(--shadow-md);
}

/* Cards */
.card {
    background: white;
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-base);
    margin-bottom: var(--spacing-lg);
}

.card:hover {
    box-shadow: var(--shadow-md);
    border-color: var(--color-primary-light);
    transform: translateY(-2px);
}

.card-header {
    border-bottom: 2px solid var(--color-border);
    padding-bottom: var(--spacing-md);
    margin-bottom: var(--spacing-md);
}

.card-header h3 {
    margin: 0;
    font-size: 1.25rem;
}

.card-body {
    padding: var(--spacing-md);
}

/* Forms */
.form-group {
    margin-bottom: var(--spacing-lg);
}

.form-label {
    display: block;
    margin-bottom: var(--spacing-sm);
    font-weight: 600;
    color: var(--color-dark);
    font-size: 0.95rem;
}

.form-control,
.shiny-input-container input,
.shiny-input-container select,
.shiny-input-container textarea {
    width: 100%;
    padding: 0.75rem 1rem;
    border: 2px solid var(--color-border);
    border-radius: var(--border-radius-md);
    font-size: 0.95rem;
    font-family: inherit;
    transition: all var(--transition-base);
    background-color: white;
}

.form-control:hover,
.shiny-input-container input:hover,
.shiny-input-container select:hover {
    border-color: #D0D0D0;
}

.form-control:focus,
.shiny-input-container input:focus,
.shiny-input-container select:focus,
.shiny-input-container textarea:focus {
    outline: none;
    border-color: var(--color-primary);
    box-shadow: 0 0 0 4px var(--color-primary-light);
}

/* Alerts */
.alert {
    padding: var(--spacing-md) var(--spacing-lg);
    border-radius: var(--border-radius-md);
    margin-bottom: var(--spacing-lg);
    border-left: 4px solid;
    animation: slideIn 0.3s ease;
}

.alert-success {
    background-color: #D4EDDA;
    border-left-color: var(--color-success);
    color: #155724;
}

.alert-danger {
    background-color: #F8D7DA;
    border-left-color: var(--color-danger);
    color: #721C24;
}

.alert-warning {
    background-color: #FFF3CD;
    border-left-color: var(--color-warning);
    color: #856404;
}

.alert-info {
    background-color: #D1ECF1;
    border-left-color: var(--color-info);
    color: #0C5460;
}

/* Layout */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-xl);
}

.row {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--spacing-lg);
}

/* Sidebar */
.sidebar {
    background: white;
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-lg);
    box-shadow: var(--shadow-sm);
    height: fit-content;
    position: sticky;
    top: var(--spacing-xl);
}

/* Navigation */
.nav-item {
    padding: var(--spacing-sm) var(--spacing-md);
    margin-bottom: var(--spacing-sm);
    border-radius: var(--border-radius-md);
    cursor: pointer;
    transition: all var(--transition-fast);
    border-left: 3px solid transparent;
}

.nav-item:hover {
    background-color: var(--color-primary-light);
    border-left-color: var(--color-primary);
}

.nav-item.active {
    background: linear-gradient(90deg, var(--color-primary-light) 0%, transparent 100%);
    border-left-color: var(--color-primary);
    color: var(--color-primary);
    font-weight: 600;
}

/* Stat Box */
.stat-box {
    background: linear-gradient(135deg, white 0%, var(--color-light) 100%);
    border: 1px solid var(--color-border);
    border-radius: var(--border-radius-lg);
    padding: var(--spacing-lg);
    text-align: center;
    transition: all var(--transition-base);
    box-shadow: var(--shadow-sm);
}

.stat-box:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--color-primary);
}

.stat-box-icon {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-md);
}

.stat-box-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--color-dark);
    margin-bottom: var(--spacing-sm);
}

.stat-box-value {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--color-primary);
}

/* Section Header */
.section-header {
    margin-bottom: var(--spacing-2xl);
    padding-bottom: var(--spacing-lg);
    border-bottom: 2px solid var(--color-border);
}

.section-header h2 {
    margin: 0 0 var(--spacing-sm) 0;
}

.section-header p {
    margin: 0;
    color: var(--color-gray);
    font-size: 0.95rem;
}

/* Animations */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-20px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.5; }
}

.fade-in {
    animation: fadeIn 0.3s ease;
}

.slide-in {
    animation: slideIn 0.3s ease;
}

.spin {
    animation: spin 1s linear infinite;
}

.pulse {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

/* Badges */
.badge {
    display: inline-block;
    padding: 0.35rem 0.75rem;
    border-radius: var(--border-radius-xl);
    font-size: 0.8rem;
    font-weight: 600;
}

.badge-primary {
    background-color: var(--color-primary-light);
    color: var(--color-primary);
}

.badge-success {
    background-color: rgba(40, 167, 69, 0.1);
    color: var(--color-success);
}

.badge-danger {
    background-color: rgba(220, 53, 69, 0.1);
    color: var(--color-danger);
}

/* Responsive */
@media (max-width: 768px) {
    h1 { font-size: 1.75rem; }
    h2 { font-size: 1.5rem; }
    h3 { font-size: 1.25rem; }
    
    .container {
        padding: var(--spacing-lg);
    }
    
    .row {
        grid-template-columns: 1fr;
    }
    
    .btn {
        width: 100%;
    }
    
    .sidebar {
        position: static;
    }
}

/* Loading Spinner */
.spinner {
    border: 4px solid var(--color-light);
    border-top: 4px solid var(--color-primary);
    border-radius: 50%;
    width: 40px;
    height: 40px;
    animation: spin 1s linear infinite;
    margin: 0 auto;
}

/* Utility Classes */
.text-center { text-align: center; }
.text-muted { color: var(--color-gray); }
.text-primary { color: var(--color-primary); }
.text-danger { color: var(--color-danger); }
.text-success { color: var(--color-success); }

.mb-sm { margin-bottom: var(--spacing-sm); }
.mb-md { margin-bottom: var(--spacing-md); }
.mb-lg { margin-bottom: var(--spacing-lg); }

.mt-sm { margin-top: var(--spacing-sm); }
.mt-md { margin-top: var(--spacing-md); }
.mt-lg { margin-top: var(--spacing-lg); }

.p-sm { padding: var(--spacing-sm); }
.p-md { padding: var(--spacing-md); }
.p-lg { padding: var(--spacing-lg); }

/* Accessibility */
:focus-visible {
    outline: 2px solid var(--color-primary);
    outline-offset: 2px;
}

/* Navbar */
.navbar {
    background: white;
    box-shadow: var(--shadow-md);
    border-bottom: 1px solid var(--color-border);
    position: fixed;
    top: 0;
    width: 100%;
    z-index: 1000;
}

.navbar-nav {
    display: flex;
    gap: var(--spacing-lg);
}

.nav-link {
    padding: var(--spacing-md) var(--spacing-lg);
    color: var(--color-dark);
    transition: all var(--transition-fast);
    font-weight: 500;
}

.nav-link:hover,
.nav-link.active {
    color: var(--color-primary);
    border-bottom: 2px solid var(--color-primary);
}
"""
