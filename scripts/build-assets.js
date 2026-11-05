#!/usr/bin/env node
/**
 * Apache OpenJPA Documentation Asset Builder
 * ==========================================
 * This script generates static assets from npm packages.
 * Assets are created locally and included in the Pelican build output
 * under the theme's static directory (emitted by Pelican to output/theme/).
 * DO NOT commit these generated files to version control.
 */

const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { execSync } = require('child_process');

// PROJECT_ROOT is the parent of the scripts directory
const PROJECT_ROOT = path.dirname(__dirname);
const CSS_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static', 'css');
const JS_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static', 'js');
const FONTS_DIR = path.join(PROJECT_ROOT, 'theme', 'apache', 'static', 'fonts');

/** Calculate SRI hash for integrity attribute */
function calculateSRI(filepath) {
  const content = fs.readFileSync(filepath);
  const hash = crypto.createHash('sha384').update(content).digest('base64');
  return `sha384-${hash}`;
}

/** Copy file with directory creation */
function copyFile(src, dest) {
  const destDir = path.dirname(dest);
  if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });
  fs.copyFileSync(src, dest);
  return dest;
}

console.log('🔨 Apache OpenJPA Documentation Asset Builder\n');

let results = {};

// 1. Bootstrap CSS
const bootstrapCssSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap', 'dist', 'css', 'bootstrap.min.css');
const bootstrapCssDest = path.join(CSS_DIR, 'bootstrap.min.css');
if (fs.existsSync(bootstrapCssSrc)) {
  copyFile(bootstrapCssSrc, bootstrapCssDest);
  results.bootstrap_css = { path: bootstrapCssDest, integrity: calculateSRI(bootstrapCssDest) };
  console.log('✓ Copied Bootstrap CSS (bootstrap.min.css)');
} else {
  console.warn('⚠ Bootstrap CSS not found - run "npm install" first');
}

// 2. Bootstrap JS
const bootstrapJsSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap', 'dist', 'js', 'bootstrap.bundle.min.js');
const bootstrapJsDest = path.join(JS_DIR, 'bootstrap.bundle.min.js');
if (fs.existsSync(bootstrapJsSrc)) {
  copyFile(bootstrapJsSrc, bootstrapJsDest);
  results.bootstrap_js = { path: bootstrapJsDest, integrity: calculateSRI(bootstrapJsDest) };
  console.log('✓ Copied Bootstrap JS (bootstrap.bundle.min.js)');
} else {
  console.warn('⚠ Bootstrap JS not found - run "npm install" first');
}

// 3. Bootstrap Icons CSS
const iconsCssSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap-icons', 'font', 'bootstrap-icons.css');
const iconsCssDest = path.join(CSS_DIR, 'bootstrap-icons.css');
if (fs.existsSync(iconsCssSrc)) {
  let css = fs.readFileSync(iconsCssSrc, 'utf8');
  // Fonts are placed in static/fonts while the CSS sits in static/css, so the
  // stock "./fonts/..." URLs (relative to the CSS) would resolve to css/fonts.
  // Rewrite them to "../fonts/..." so the icon font is found in the built site.
  css = css.replace(/url\(["']?\.\/fonts\//g, 'url("../fonts/');
  fs.writeFileSync(iconsCssDest, css);
  console.log('✓ Copied Bootstrap Icons CSS (font paths normalized)');
}

// 4. Bootstrap Icons fonts
const iconsFontsSrc = path.join(PROJECT_ROOT, 'node_modules', 'bootstrap-icons', 'font', 'fonts');
if (fs.existsSync(iconsFontsSrc)) {
  if (!fs.existsSync(FONTS_DIR)) fs.mkdirSync(FONTS_DIR, { recursive: true });
  const fontFiles = fs.readdirSync(iconsFontsSrc);
  fontFiles.forEach(file => {
    if (file.endsWith('.woff2') || file.endsWith('.woff') || file.endsWith('.ttf')) {
      copyFile(path.join(iconsFontsSrc, file), path.join(FONTS_DIR, file));
    }
  });
  console.log(`✓ Copied ${fontFiles.length} Bootstrap Icons font files`);
} else {
  console.warn('⚠ Bootstrap Icons fonts not found');
}

// 5. Vendor highlight.js locally, bundling the "common" language set via esbuild
//    into a single self-contained UMD-style file exposing window.hljs.
try {
  const hljsBundleOut = path.join(JS_DIR, 'highlight', 'highlight.js');
  fs.mkdirSync(path.dirname(hljsBundleOut), { recursive: true });
  const esbuild = path.join(PROJECT_ROOT, 'node_modules', '.bin', 'esbuild');
  execSync(
    `${JSON.stringify(esbuild)} ${JSON.stringify(
      path.join(PROJECT_ROOT, 'node_modules', 'highlight.js', 'lib', 'common.js')
    )} --bundle --format=iife --global-name=hljs --minify --outfile=${JSON.stringify(hljsBundleOut)}`,
    { stdio: ['ignore', 'ignore', 'pipe'] }
  );
  results.highlight_js = { path: hljsBundleOut, integrity: calculateSRI(hljsBundleOut) };
  console.log('✓ Built local highlight.js bundle (js/highlight/highlight.js) with common languages');

  // Copy a highlight.js theme (light) for syntax colors
  const hljsThemeSrc = path.join(PROJECT_ROOT, 'node_modules', 'highlight.js', 'styles', 'github.min.css');
  const hljsThemeDest = path.join(CSS_DIR, 'highlight.css');
  if (fs.existsSync(hljsThemeSrc)) {
    copyFile(hljsThemeSrc, hljsThemeDest);
    console.log('✓ Copied highlight.js theme (github.min.css -> css/highlight.css)');
  }
} catch (e) {
  console.warn('⚠ highlight.js bundling failed - run "npm install" first (esbuild + highlight.js): ' + (e.message || e));
}

// 6. Integrity JSON for templates
const integrityData = {
  bootstrap_css: results.bootstrap_css?.integrity || 'sha384-PLACEHOLDER',
  bootstrap_js: results.bootstrap_js?.integrity || 'sha384-PLACEHOLDER',
  highlight_js: results.highlight_js?.integrity || '',
  generated: new Date().toISOString()
};
fs.writeFileSync(
  path.join(PROJECT_ROOT, 'theme', 'apache', 'static', 'integrity.json'),
  JSON.stringify(integrityData, null, 2)
);
console.log('✓ Generated integrity.json');

console.log('\n📁 Generated Assets:');
console.log(`  CSS:  theme/apache/static/css/`);
console.log(`  JS:   theme/apache/static/js/`);
console.log(`  Fonts: theme/apache/static/fonts/`);
console.log(`  Integrity: theme/apache/static/integrity.json`);

console.log('\n💡 Template Variables:');
console.log(`  bootstrap_css_integrity = ${integrityData.bootstrap_css}`);
console.log(`  bootstrap_js_integrity = ${integrityData.bootstrap_js}`);

console.log('\n✅ Build complete! These files are now ready for Pelican.');