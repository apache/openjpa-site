#!/usr/bin/env node
/**
 * Development server for Apache OpenJPA documentation
 * Combines file watching with Pelican live-reload server
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { spawn } = require('child_process');
const chokidar = require('chokidar');

const PROJECT_ROOT = __dirname;
const STATIC_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static');
const CONTENT_DIR = path.join(PROJECT_ROOT, 'content');

const CSS_DIR = path.join(STATIC_DIR, 'css');
const JS_DIR = path.join(STATIC_DIR, 'js');

let pelicanProcess = null;

function log(message) {
  const timestamp = new Date().toLocaleTimeString();
  console.log(`[${timestamp}] ${message}`);
}

function copyAssets() {
  const bootstrapCssSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap', 'dist', 'css', 'bootstrap.min.css');
  const bootstrapJsSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap', 'dist', 'js', 'bootstrap.bundle.min.js');

  // Ensure directories exist
  if (!fs.existsSync(CSS_DIR)) fs.mkdirSync(CSS_DIR, { recursive: true });
  if (!fs.existsSync(JS_DIR)) fs.mkdirSync(JS_DIR, { recursive: true });

  if (fs.existsSync(bootstrapCssSrc)) {
    fs.copyFileSync(bootstrapCssSrc, path.join(CSS_DIR, 'bootstrap.min.css'));
  }

  if (fs.existsSync(bootstrapJsSrc)) {
    fs.copyFileSync(bootstrapJsSrc, path.join(JS_DIR, 'bootstrap.bundle.min.js'));
  }

  // Generate hashes
  const cssHash = crypto.createHash('sha384').update(fs.readFileSync(path.join(CSS_DIR, 'bootstrap.min.css'))).digest('base64');
  const jsHash = crypto.createHash('sha384').update(fs.readFileSync(path.join(JS_DIR, 'bootstrap.bundle.min.js'))).digest('base64');

  fs.writeFileSync(
    path.join(STATIC_DIR, 'integrity.json'),
    JSON.stringify({
      bootstrap_css: `sha384-${cssHash}`,
      bootstrap_js: `sha384-${jsHash}`,
      timestamp: new Date().toISOString()
    }, null, 2)
  );
}

function startPelicanServer() {
  log('Starting Pelican development server...');

  if (pelicanProcess) {
    pelicanProcess.kill();
  }

  pelicanProcess = spawn('pelican', ['content', '-s', 'pelican.auto.py', '-l'], {
    cwd: PROJECT_ROOT,
    stdio: 'inherit',
    env: { ...process.env, BROWSER: 'open' }
  });

  pelicanProcess.on('exit', (code) => {
    if (code !== 0) {
      log(`Pelican server exited with code ${code}`);
      setTimeout(startPelicanServer, 1000);
    }
  });
}

// Initialize
console.log('\n🚀 OpenJPA Documentation Development Server\n');
console.log('Features:');
console.log('  ✓ Watches content and asset changes');
console.log('  ✓ Auto-rebuilds with Pelican live-reload');
console.log('  ✓ Serves at http://localhost:8000\n');
console.log('Press Ctrl+C to stop\n');

// Copy initial assets
copyAssets();

// Start Pelican server
startPelicanServer();

// Watch content files
const watcher = chokidar.watch(CONTENT_DIR, {
  ignored: ['**/node_modules/**', '**/.git/**'],
  ignoreInitial: true
});

watcher.on('all', (event, filePath) => {
  const ext = path.extname(filePath);
  if (['.md', '.markdown', '.html'].includes(ext)) {
    log(`Content ${event}: ${path.basename(filePath)}`);
  }
});

// Watch static assets
const staticWatcher = chokidar.watch(path.join(STATIC_DIR, '**/*.{css,js}'), {
  ignored: ['**/node_modules/**', '**/.git/**'],
  ignoreInitial: true
});

staticWatcher.on('all', (event, filePath) => {
  log(`Asset ${event}: ${path.basename(filePath)}`);
});

// Graceful shutdown
process.on('SIGINT', () => {
  console.log('\n\n👋 Shutting down...');
  if (pelicanProcess) pelicanProcess.kill();
  process.exit(0);
});

process.on('SIGTERM', () => {
  if (pelicanProcess) pelicanProcess.kill();
  process.exit(0);
});
