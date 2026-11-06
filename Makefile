# ============================================================================
# Makefile for Apache OpenJPA Documentation Site
# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

# Apache OpenJPA Documentation Build Configuration
# Usage: make [target]

SHELL := /bin/bash
.PHONY: help install prepare dev build clean venv

# Default target
.DEFAULT_GOAL := help

## help: Show this help message
help:
	@echo "Apache OpenJPA Documentation Build Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  install    - Create venv and install all dependencies (Python + npm)"
	@echo "  prepare    - Build static assets from npm packages"
	@echo "  dev        - Development build with live reload"
	@echo "  build      - Production build"
	@echo "  clean      - Remove build artifacts"
	@echo "  venv       - Create Python virtual environment only"
	@echo "  help       - Show this help message"
	@echo ""
	@echo "Quick Start:"
	@echo "  make install   # First time setup"
	@echo "  make dev       # Develop locally with live reload"
	@echo "  make build     # Build for production"

## install: Create venv and install dependencies
install:
	@echo "🔧 Setting up Apache OpenJPA documentation environment..."
	@if [ ! -d venv ]; then \
		echo "📦 Creating Python virtual environment..."; \
		python3 -m venv venv; \
		echo "✅ Virtual environment created. Activate with: source venv/bin/activate"; \
	fi
	@echo "📚 Installing Python dependencies..."
	@source venv/bin/activate && pip install --upgrade pip && \
		pip install pelican markdown beautifulsoup4
	@echo "📦 Installing npm dependencies..."
	@npm install
	@echo ""
	@echo "✅ Setup complete!"
	@echo ""
	@echo "Next steps:"
	@echo "  source venv/bin/activate"
	@echo "  npm run prepare"
	@echo "  pelican content -s pelican.auto.py -l"

## prepare: Build static assets from npm packages
prepare:
	@echo "🏗️  Building static assets from npm packages..."
	@npm run prepare
	@echo "✅ Static assets built successfully"

## dev: Build and serve with live reload (regenerates on content changes)
dev: prepare
	@echo "🚀 Building site and starting live-reload server..."
	@echo "Edit content/*.md files to see changes automatically"
	@echo "Site available at http://localhost:8000 (Ctrl-C to stop)"
	@echo ""
	@source venv/bin/activate && pelican content -s pelican.auto.py -lr

## build: Production build
build: prepare
	@echo "🏢 Building production site..."
	@source venv/bin/activate && pelican content -s pelican.auto.py
	@echo "✅ Production build complete. Output in ./output/"

## clean: Remove build artifacts
clean:
	@echo "🧹 Cleaning build artifacts..."
	@rm -rf output/
	@rm -rf theme/apache/static/bundles/
	@rm -f theme/apache/static/integrity.json
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Clean complete"

## venv: Create Python virtual environment only
venv:
	@echo "📦 Creating Python virtual environment..."
	@if [ -d venv ]; then \
		echo "⚠️  venv already exists. Remove it first with 'rm -rf venv' to recreate."; \
	else \
		python3 -m venv venv && \
		echo "✅ Virtual environment created. Activate with: source venv/bin/activate"; \
	fi
