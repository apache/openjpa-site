#!/usr/bin/env node
/**
 * Build script for Apache OpenJPA documentation site assets
 * Creates cache-friendly bundles with content hashes
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

const PROJECT_ROOT = __dirname;
const STATIC_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static');
const BUNDLES_DIR = path.join(STATIC_DIR, 'bundles');

// Ensure bundles directory exists
if (!fs.existsSync(BUNDLES_DIR)) {
  fs.mkdirSync(BUNDLES_DIR, { recursive: true });
}

console.log('🔨 Building Apache OpenJPA documentation bundles...\n');

/**
 * Calculate SRI hash for a file
 */
function calculateHash(filepath) {
  const content = fs.readFileSync(filepath);
  const hash = crypto.createHash('sha256').update(content).digest('base64');
  return `sha256-${hash}`;
}

/**
 * Copy file and return its SRI hash and content hash
 */
function copyFile(src, dest) {
  const content = fs.readFileSync(src);
  const hash = crypto.createHash('sha256').update(content).digest('base64').substring(0, 8);
  fs.writeFileSync(dest, content);
  return { sri: calculateHash(src), shortHash: hash };
}

/**
 * Copy CSS file with content hashing
 */
function buildCss() {
  console.log('📦 Building vendor.css...');
  
  const bootstrapCssPath = path.join(STATIC_DIR, 'css', 'bootstrap.min.css');
  const customCssPath = path.join(STATIC_DIR, 'css', 'custom.css');
  
  if (!fs.existsSync(bootstrapCssPath)) {
    console.error('✗ Bootstrap CSS not found. Run "npm install" first.');
    return null;
  }

  // Read bootstrap CSS
  let cssContent = fs.readFileSync(bootstrapCssPath, 'utf8');
  
  // Append custom CSS
  if (fs.existsSync(customCssPath)) {
    const customCss = fs.readFileSync(customCssPath, 'utf8');
    cssContent += '\n/* Custom CSS */\n' + customCss;
  }

  // Calculate hash and write bundled file
  const hashResult = copyFile(bootstrapCssPath, path.join(BUNDLES_DIR, 'temp.css'));
  const hash = crypto.createHash('sha256').update(cssContent).digest('base64').substring(0, 8);
  const outputName = `vendor.${hash}.css`;
  
  // Write combined CSS
  fs.writeFileSync(path.join(BUNDLES_DIR, outputName), cssContent);
  
  console.log(`  ✓ Created ${outputName}`);
  
  return { filename: outputName, sri: hashResult.sri };
}

/**
 * Copy JS files with content hashing
 */
function buildJs() {
  console.log('📦 Building JS bundles...');
  
  // Vendor JS (Bootstrap)
  const bootstrapJsPath = path.join(STATIC_DIR, 'js', 'bootstrap.bundle.min.js');
  if (fs.existsSync(bootstrapJsPath)) {
    const { filename, sri } = copyFile(bootstrapJsPath, path.join(BUNDLES_DIR, 'vendor.js'));
    console.log(`  ✓ Created vendor.js`);
  } else {
    console.error('  ✗ Bootstrap JS not found');
  }

  // Highlight.js
  const highlightJsPath = path.join(STATIC_DIR, 'js', 'highlight.min.js');
  if (fs.existsSync(highlightJsPath)) {
    const hash = crypto.createHash('sha256').update(fs.readFileSync(highlightJsPath)).digest('base64').substring(0, 8);
    const outputName = `highlight.${hash}.js`;
    copyFile(highlightJsPath, path.join(BUNDLES_DIR, outputName));
    console.log(`  ✓ Created ${outputName}`);
  }

  // OpenJPA enhancements
  const docJsPath = path.join(STATIC_DIR, 'js', 'doc-enhancements.js');
  if (fs.existsSync(docJsPath)) {
    const hash = crypto.createHash('sha256').update(fs.readFileSync(docJsPath)).digest('base64').substring(0, 8);
    const outputName = `openjpa.${hash}.js`;
    copyFile(docJsPath, path.join(BUNDLES_DIR, outputName));
    console.log(`  ✓ Created ${outputName}`);
  }
}

/**
 * Main build function
 */
function buildAll() {
  try {
    const cssResult = buildCss();
    buildJs();

    // Find generated files
    const files = fs.readdirSync(BUNDLES_DIR);
    const cssFile = files.find(f => f.startsWith('vendor.') && f.endsWith('.css'));
    const jsFiles = files.filter(f => f.endsWith('.js'));

    // Generate manifest
    const manifest = {
      timestamp: new Date().toISOString(),
      assets: {}
    };

    if (cssFile) {
      manifest.assets.css = {
        vendor: cssFile,
        integrity: calculateHash(path.join(BUNDLES_DIR, cssFile))
      };
    }

    if (jsFiles.length > 0) {
      const vendorJs = jsFiles.find(f => f === 'vendor.js' || f.startsWith('vendor.'));
      if (vendorJs) {
        manifest.assets.js = {
          vendor: vendorJs,
          integrity: calculateHash(path.join(BUNDLES_DIR, vendorJs))
        };
      }
      
      const openjpaJs = jsFiles.find(f => f.startsWith('openjpa.'));
      if (openjpaJs) {
        const hash = openjpaJs.match(/openjpa\.([a-f0-9]+)\.js/)?.[1] || 'unknown';
        manifest.assets.openjpa = {
          js: openjpaJs,
          hash: hash
        };
      }
    }

    // Write manifest files
    fs.writeFileSync(
      path.join(BUNDLES_DIR, 'manifest.json'),
      JSON.stringify(manifest, null, 2)
    );

    // Create simple versions file for templates
    const versions = {
      vendorCss: manifest.assets.css?.vendor || 'vendor.css',
      vendorJs: manifest.assets.js?.vendor || 'vendor.js',
      openjpaJs: manifest.assets.openjpa?.js || 'openjpa.js',
      builtAt: manifest.timestamp
    };
    
    fs.writeFileSync(
      path.join(BUNDLES_DIR, 'versions.json'),
      JSON.stringify(versions, null, 2)
    );

    console.log('\n✅ Build complete!');
    console.log('📁 Output directory:', BUNDLES_DIR);
    console.log('\nGenerated files:');
    console.log('  - manifest.json (full metadata with SRI hashes)');
    console.log('  - versions.json (template-friendly names)');
    
    if (cssFile) console.log(`  - CSS: ${cssFile}`);
    jsFiles.forEach(f => console.log(`  - JS: ${f}`));

    return 0;
  } catch (error) {
    console.error('\n❌ Build failed:', error.message);
    console.error(error.stack);
    return 1;
  }
}

// Run build
process.exit(buildAll());