# CMS Migration

1. Markdown conversions

   - Rename from mdtext to md
   - All files must have a title
   - Switched some spans to divs
   - Included alt text for images and switched some imag tags to markdown
   - Cleaned up list indentation paticulatly in ./content/begin-using-openjpa---the-basics.md
   - Changed many fully qualified hyperlinks to openjpa.apache.org to be internal particularly on
     ./content/documentation.md

   See [changes.txt](changes.txt)

2. Theme Template

   CMS templates were converted into `base.html`

3. Configuration

   See [pelicanconf.py](../pelicanconf.py)

4. Pelican ASF plugin configuration

   [asfgenid.py](../theme/plugins/asfgenid.py)

   - 'unsafe_tags': True  # allow style, script, and iframe tags
   - 'metadata': False    # no metadata replacement in markdown files
   - 'elements': False    # CMS didn't use mdx_elementid featuresz
   - 'headings': True     # Fix up headings w/ permalinks
   - 'headings_re': r'^h[1-4]'
   - 'permalinks': True,
   - 'toc': False         # does not use [TOC]
   - 'toc_headers': r"h[1-4]",
   - 'tables': True       # Fix up for markdown table class

5. Documentation branches

   Setup two branches for documentation that is updated separately from the main site.

   - *builds* branch has the documentation from TLP releases.
   - *docs* branch has the documentation from Incubating releases.
