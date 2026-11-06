# Apache OpenJPA Documentation Site - Build Process

This project uses an npm-based build process to manage embedded assets (CSS, JS) for the documentation site.

## Prerequisites

- Node.js 22.x or later
- Python 3.11+
- pip

## Setup

1. Install Python dependencies:
```bash
pip install pelican markdown
pip install -r requirements.txt
```

2. Install npm dependencies:
```bash
npm install
```

## Building the Site

### Development Build
```bash
npm run build:dev
```
This builds the content without asset processing.

### Full Build (Production)
```bash
npm run build
```
This builds both the content and processes all static assets.

### Build Assets Only
```bash
node scripts/build-assets.js
```

## Asset Processing

The `build-assets.js` script:
1. Copies Bootstrap 5.3.3 CSS and JS to `theme/apache/static/`
2. Copies Highlight.js 11.10.0 to `theme/apache/static/js/`
3. Copies Bootstrap Icons to `theme/apache/static/fonts/`
4. Generates SRI integrity hashes for CSP compliance
5. Creates `integrity.json` for template injection

## CI/CD

The site is automatically built and deployed via GitHub Actions on push to `main`.

## Apache Compliance Notes

- All external resources are now embedded locally
- SRI integrity hashes are generated for security
- CSP headers are configured in `.htaccess`
- No external CDNs are used
- All code is Apache License 2.0 compliant

## Project Structure

```
project-root/
├── package.json           # npm dependencies and scripts
├── package-lock.json      # locked npm dependencies
├── pelican.auto.py        # Pelican configuration
├── scripts/
│   └── build-assets.js    # Asset build script
├── theme/apache/
│   ├── templates/
│   │   ├── base.html      # Main template with embedded CSS/JS
│   │   ├── page.html      # Page template with breadcrumb
│   │   └── styles.css     # Custom CSS
│   └── static/            # Generated during build
│       ├── css/
│       ├── js/
│       ├── fonts/
│       └── integrity.json # Generated SRI hashes
├── content/               # Documentation content (Markdown)
├── doap.rdf               # Apache DOAP file for project metadata
├── .asf.yaml              # Apache build configuration
└── .github/workflows/
    └── build.yml          # GitHub Actions workflow
```
