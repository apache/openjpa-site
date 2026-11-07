#!/usr/bin/env node
/**
 * Watch script for development
 * Watches files and rebuilds Pelican site on changes
 */

const fs = require('fs');
const path = require('path');
const { spawn } = require('child_process');
const chokidar = require('chokidar');

const PROJECT_ROOT = path.dirname(__dirname);
const CONTENT_DIR = path.join(PROJECT_ROOT, 'content');
const STATIC_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static');

let pelicanProcess = null;
let isBuilding = false;

function log(message) {
  console.log(`[${new Date().toISOString()}] ${message}`);
}

function startPelicanWatch() {
  log('🔨 Starting Pelican rebuild...');

  if (pelicanProcess) {
    pelicanProcess.kill();
    pelicanProcess = null;
  }

  pelicanProcess = spawn('pelican', ['content', '-s', 'pelican.auto.py', '-l'], {
    cwd: PROJECT_ROOT,
    stdio: 'pipe'
  });

  pelicanProcess.stdout.on('data', (data) => {
    process.stdout.write(data.toString());
  });

  pelicanProcess.stderr.on('data', (data) => {
    process.stderr.write(data.toString());
  });
}

// Initial build
log('🚀 Starting development watch mode...\n');

// Watch content directory
chokidar.watch(path.join(CONTENT_DIR, '**/*.md'), {
  ignored: /node_modules|\.git/,
  persistent: true
}).on('change', (filePath) => {
  if (!isBuilding) {
    log(`📝 Content changed: ${path.relative(CONTENT_DIR, filePath)}`);
    startPelicanWatch();
  }
}).on('add', (filePath) => {
  if (!isBuilding) {
    log(`📝 File added: ${path.relative(CONTENT_DIR, filePath)}`);
    startPelicanWatch();
  }
});

// Watch static assets
chokidar.watch(path.join(STATIC_DIR, '**/*.{css,js}')).on('change', (filePath) => {
  if (!isBuilding) {
    log(`🎨 Asset changed: ${path.relative(STATIC_DIR, filePath)}`);
  }
});

// Watch package.json
chokidar.watch('package.json').on('change', () => {
  if (!isBuilding) {
    log('📦 package.json changed');
  }
});

// Also watch pelican config files
chokidar.watch(['pelican.auto.py', 'pelicanconf.yaml']).on('change', () => {
  if (!isBuilding) {
    log('⚙️ Configuration changed');
    startPelicanWatch();
  }
});

// Handle shutdown
process.on('SIGINT', () => {
  log('\n\n👋 Shutting down watcher...');
  if (pelicanProcess) {
    pelicanProcess.kill();
  }
  process.exit(0);
});

process.on('SIGTERM', () => {
  if (pelicanProcess) {
    pelicanProcess.kill();
  }
  process.exit(0);
});

log('👁️ Watching for changes...');
log('   Content: ' + CONTENT_DIR);
log('   Static:  ' + STATIC_DIR + '\n');
