#!/usr/bin/python -B
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.
# ============================================================================
# asfsearch.py -- Pelican plugin that writes a client-side search index
# (search-index.json) into the output tree.
#
# The index is a flat JSON array of { title, url, section, text } objects
# covering every rendered page.  The theme's search box fetches this file
# and filters it in the browser, keeping the search fully static and local
# (no external service, CSP-safe: the JSON is fetched, never executed).
# ============================================================================

import os
import re
import json
import traceback

import pelican.plugins.signals

# Strip HTML tags but keep meaningful whitespace between block elements so
# words from adjacent blocks do not run together.
TAG_RE = re.compile(r'<(script|style)[^>]*>.*?</\1>', re.IGNORECASE | re.DOTALL)
BLOCK_RE = re.compile(r'<[^>]+>')
WS_RE = re.compile(r'\s+')

# Pseudo-pages / technical artifacts that should not appear in search results
# but also no harm if they do; we keep them in but weight them low.
SKIP_URL_SUFFIXES = ()


def to_plain_text(html):
    """Best-effort HTML -> plain text for indexing."""
    if not html:
        return ''
    text = TAG_RE.sub(' ', html)
    text = BLOCK_RE.sub(' ', text)
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&#39;', "'").replace('&quot;', '"')
    text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>')
    # link char permalinks plugin uses
    text = text.replace('¶', ' ')
    text = WS_RE.sub(' ', text)
    return text.strip()


def _gather(generator, index):
    pages = getattr(generator, 'pages', None) or []
    for page in pages:
        url = getattr(page, 'url', '') or ''
        if url == 'index.html':
            continue
        title = (getattr(page, 'title', '') or '').strip()
        text = to_plain_text(getattr(page, '_content', '') or '')
        index.append({
            'title': title,
            'url': url,
            'section': 'Documentation',
            'text': text[:8000],
        })


def write_search_index(generator):
    """Write search-index.json once the page generator is finalized."""
    try:
        index = []
        _gather(generator, index)

        output_path = getattr(generator, 'output_path', None) or generator.settings.get('OUTPUT_PATH')
        if not output_path:
            return

        os.makedirs(output_path, exist_ok=True)
        dest = os.path.join(output_path, 'search-index.json')
        with open(dest, 'w', encoding='utf-8') as fh:
            json.dump(index, fh, ensure_ascii=False, separators=(',', ':'))
        print(f'  search-index.json ({len(index)} entries)')
    except Exception:
        print('-----', file=__import__('sys').stderr)
        print('FATAL: asfsearch.write_search_index', file=__import__('sys').stderr)
        traceback.print_exc()


def register():
    pelican.plugins.signals.page_generator_finalized.connect(write_search_index)