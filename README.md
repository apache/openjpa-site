# Apache OpenJPA Documentation Site

This repository contains the documentation for Apache OpenJPA, a Java persistence project at The Apache Software Foundation.

## Building the Site

### Prerequisites

- **Node.js** 22.x or later
- **Python** 3.12+
- **pip** (Python package manager)
- **make** (optional, for convenience)

### Setting up the Development Environment

Since your environment has PEP 668 (externally-managed environment), you need to use a virtual environment:

```bash
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
# venv\Scripts\activate
```

### Installing Dependencies

The easiest way to install all dependencies (Python + npm) is the `install` Make target, which creates a virtual environment and installs everything:

```bash
make install
```

This performs the equivalent of:

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pelican markdown beautifulsoup4
npm install
```

You do NOT need to activate the virtual environment manually: the `dev` and `build` Make targets handle activation for you.

### Building the Site

The recommended workflow uses the Make targets:

#### Development Build (with live reload)
```bash
make dev
```

`make dev` builds the static assets (Bootstrap CSS/JS from npm packages) and starts Pelican with live reload at http://localhost:8000.

#### Production Build
```bash
make build
```

`make build` builds the static assets and produces the final site in the `output/` directory.

#### Manual build (advanced)

If you prefer to run the underlying commands directly:

```bash
# Build static assets first (required - missing assets cause a 'no index file' error)
npm run prepare

# Development (with live reload)
source venv/bin/activate
pelican content -s pelican.auto.py
pelican content -s pelican.auto.py -lr

# Production
source venv/bin/activate
pelican content -s pelican.auto.py
```

> **Important:** Always run `npm run prepare` before `pelican`. The generated static assets in `theme/apache/static/` are gitignored and only exist after that step, so skipping it leaves the favicon/logo referencing files that are not yet present.

### Output Location

The built site will be in the `output/` directory. To serve locally:

```bash
# Preview the built site
python3 -m http.server 8000 -d output/
# Visit http://localhost:8000
```

## Project Structure

```
project-root/
├── content/           # Documentation source files (Markdown)
├── theme/
│   └── apache/        # Template files and styling
│       ├── templates/
│       │   ├── base.html      # Main template
│       │   ├── page.html      # Page template
│       │   └── styles.css     # Custom CSS
│       └── static/             # Generated during build
│           ├── css/
│           ├── js/
│           └── fonts/
├── scripts/           # Build scripts
│   ├── build-assets.js         # Asset bundler
│   ├── watch.js                # Watch mode
│   └── serve.js                # Development server
├── output/            # Generated site (gitignored)
├── package.json       # npm configuration
├── requirements.txt   # Python dependencies
├── pelican.auto.py     # Pelican configuration
├── .asf.yaml          # ASF repository and website configuration
└── Makefile           # Convenience build commands
```

## Development Workflow

1. **Edit content** in `content/*.md`
2. **Run `make dev`** to build assets and preview with live reload at http://localhost:8000
3. **Run `make build`** to produce the production site in `output/`
4. **Open a pull request**: CI builds the site for every pull request

## Publishing

The site is built and published with GitHub Actions; the ASF Pelican buildbot is not used
(do not add a `pelican:` block to `.asf.yaml`, it would overwrite the published site).

| Site | Branch | How it gets there |
|------|--------|-------------------|
| https://openjpa.apache.org/ | `asf-site` | every push to `main` (`build.yml`) |
| https://openjpa.staged.apache.org/ | `asf-staging` | manually: Actions → *Publish staging website* → choose a branch |

Both workflows build the site and copy `output/` into the `output/` directory of the target branch.
Each target branch has its own `.asf.yaml` (`publish:` resp. `staging:`); the blocks in `main`'s
`.asf.yaml` have no effect there.

### Deploying a staged version

Use the staging site to show a change (or a snapshot of the current state) before it goes live:

1. Push your branch to `apache/openjpa-site` (the workflow cannot publish from a fork). The branch must
   contain `.github/workflows/publish-staging.yml`, so base it on a current `main`.
2. Open *Actions* → *Publish staging website* → *Run workflow*, select your branch and run it.
3. After a minute or two the result is at https://openjpa.staged.apache.org/.

The staging site always shows the last published branch; running the workflow on `main` resets it.

### Deploying the live site

Merge the pull request into `main`. The `deploy` job of `build.yml` publishes the result to `asf-site`,
and https://openjpa.apache.org/ is updated a few minutes later. To publish again without a change,
run *Build and Deploy Apache OpenJPA Documentation* on `main` from the *Actions* tab.

## Apache Compliance

All resources are either:
- **Embedded locally**: Bootstrap CSS/JS from npm packages
- **Apache-approved CDN**: jsdelivr for Highlight.js (documentation library)

No external CDNs are used for critical assets.

## Repository Settings

Description, homepage and topics of the GitHub repository are set in `.asf.yaml` (`github:` section,
topics as `labels`); changes made in the GitHub settings are overwritten.

## Troubleshooting

### PEP 668 Error
If you see "externally-managed-environment" error:
```bash
# Create and use virtual environment
python3 -m venv venv
source venv/bin/activate
pip install pelican markdown beautifulsoup4
```

### Missing Bootstrap Files
If CSS/JS files are missing:
```bash
make prepare
```

Or manually:
```bash
npm install
npm run prepare
```

### Live Reload Not Working
```bash
# The dev target rebuilds assets and serves with live reload
make dev
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run `npm run prepare` to update assets (or `make build` to build and verify)
5. Commit and push
6. Open a pull request

## License

Licensed under the Apache License, Version 2.0. See the LICENSE file for details.
