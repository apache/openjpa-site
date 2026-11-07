
# ============================================================================
# Apache OpenJPA Documentation Site Configuration
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

# ============================================================================
# Asset Bundled Configuration
# These values are used by the build process to inject bundle info
# The build-assets.js script generates integrity.json with hashes
# ============================================================================

# ============================================================================
# Basic Pelican Settings
# ============================================================================
SITENAME = 'Apache OpenJPA'
SITEDESC = 'Apache OpenJPA is a Java persistence project at The Apache Software Foundation'
SITEDOMAIN = 'openjpa.apache.org'
SITEURL = 'https://openjpa.apache.org'
SITELOGO = 'https://openjpa.apache.org/images/openjpa-logo.png'
SITEREPOSITORY = 'https://github.com/apache/openjpa-site/blob/main/content/'
CURRENTYEAR = 2026
TRADEMARKS = 'Apache, the Apache feather logo, and "Project" are trademarks or registered trademarks'
TIMEZONE = 'UTC'

# Theme configuration
THEME = './theme/apache'

# Plugins
PLUGIN_PATHS = ['./theme/plugins']
PLUGINS = ['asfgenid', 'asfsearch']

# Static content paths
PAGE_PATHS = ['.']
STATIC_PATHS = ['.', 'static']

# Page settings
PATH_METADATA = r'(?P<path_no_ext>.*)\..*'
PAGE_SAVE_AS = '{path_no_ext}.html'
PAGE_URL = '{path_no_ext}.html'
PAGE_TRANSLATION_ID = None

# Default date settings - all pages without date will use current date
DEFAULT_DATE = 'fs'  # Use file system date
DEFAULT_DATE_FORMAT = '%Y-%m-%d'

# Disable articles (we only use pages)
ARTICLE_PATHS = []
ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'
ARTICLE_TRANSLATION_ID = None

# Disabled features
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''

# Disable HTML processing
READERS = {'html': None}

# ============================================================================
# Template context variables for Bootstrap integrity hashes
# ============================================================================
bootstrap_css_integrity = 'sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB'
bootstrap_js_integrity = 'sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI'
SITEURL = 'https://openjpa.apache.org'

# ============================================================================
# Configure the asfgenid plugin
# ============================================================================
ASF_GENID = {
 'unsafe_tags': True,
 'metadata': False,
 'elements': False,
 'permalinks': True,
 'tables': False,
 'headings': True,
 'headings_re': '^h[1-4]',
 'toc': True,
 'toc_headers': '^h[1-4]',
 'debug': False,
}








