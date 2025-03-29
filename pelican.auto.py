
# Basic information about the site.
SITENAME = 'Apache OpenJPA'
SITEDESC = 'Apache OpenJPA is a Java persistence project at The Apache Software Foundation'
SITEDOMAIN = 'openjpa.apache.org'
SITEURL = 'https://openjpa.apache.org'
SITELOGO = 'https://openjpa.apache.org/images/openjpa-logo.png'
SITEREPOSITORY = 'https://github.com/apache/openjpa-site/blob/main/content/'
CURRENTYEAR = 2025
TRADEMARKS = 'Apache, the Apache feather logo, and "Project" are trademarks or registered trademarks'
TIMEZONE = 'UTC'
# Theme includes templates and possibly static files
THEME = './theme/apache'
# Specify location of plugins, and which to use
PLUGIN_PATHS = [ '/home/solomax/work/_oss/site-pelican/infrastructure-pelican/bin/../plugins', './theme/plugins',  ]
PLUGINS = [ 'gfm', 'asfgenid',  ]
# All content is located at '.' (aka content/ )
PAGE_PATHS = [ '.' ]
STATIC_PATHS = [ '.',  ]
# Where to place/link generated pages

PATH_METADATA = '(?P<path_no_ext>.*)\\..*'

PAGE_SAVE_AS = '{path_no_ext}.html'
# Don't try to translate
PAGE_TRANSLATION_ID = None
# Disable unused Pelican features
# N.B. These features are currently unsupported, see https://github.com/apache/infrastructure-pelican/issues/49
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
# Disable articles by pointing to a (should-be-absent) subdir
ARTICLE_PATHS = [ 'blog' ]
# needed to create blogs page
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# Disable all processing of .html files
READERS = { 'html': None, }

# Configure the asfgenid plugin
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








