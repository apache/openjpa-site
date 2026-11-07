/*
 * ============================================================================
 * Apache OpenJPA Documentation Enhancement Scripts
 * Licensed to the Apache Software Foundation (ASF) under one or more
 * contributor license agreements.
 * ============================================================================
 *
 * Provides: TOC scroll highlighting, code-block copy buttons, smooth scroll,
 * scroll progress bar, and search. The site uses a single light theme.
 * All assets local; no external CDN. The highlight.js core is loaded from the
 * local bundle (window.hljs) in <base.html> before this script.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initToc();
    initCopyButtons();
    initSmoothScroll();
    initScrollProgress();
    highlightCode();
    initActiveNavLink();
    initLanguageLabels();
    initSearch();
  });

  function ready(fn) {
    if (document.readyState !== 'loading') {
      fn();
    } else {
      document.addEventListener('DOMContentLoaded', fn);
    }
  }

  /* ------------------------------------------------------------------ *
   * TOC active-state highlighting as the reader scrolls
   * ------------------------------------------------------------------ */
  function initToc() {
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll('.bd-toc a'));
    var headings = document.querySelectorAll('h1[id], h2[id], h3[id], h4[id], h5[id], h6[id]');
    if (!headings.length) { return; }

    function setActive(id) {
      tocLinks.forEach(function (link) {
        var lk = link;
        lk.classList.toggle('active', lk.getAttribute('href') === '#' + id);
      });
    }

    if ('IntersectionObserver' in window) {
      var observer = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { setActive(entry.target.id); }
        });
      }, { rootMargin: '-15% 0px -40% 0px', threshold: 0 });

      Array.prototype.forEach.call(headings, function (h) { observer.observe(h); });
    } else {
      // Fallback: highlight based on current hash
      setActive(location.hash.substring(1));
    }
  }

  /* ------------------------------------------------------------------ *
   * Copy-to-clipboard button on code blocks
   * ------------------------------------------------------------------ */
  function initCopyButtons() {
    var blocks = document.querySelectorAll('pre code');
    if (!blocks.length || !('clipboard' in navigator) && !document.execCommand) {
      return;
    }
    Array.prototype.forEach.call(blocks, function (block) {
      var pre = block.parentElement;
      if (pre.querySelector('.copy-btn')) { return; }
      var btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Copy code to clipboard');
      btn.textContent = 'Copy';

      btn.addEventListener('click', function () {
        copyText(block.textContent, btn);
      });

      pre.style.position = 'relative';
      pre.appendChild(btn);
    });
  }

  function copyText(text, btn) {
    function done() {
      var original = btn.textContent;
      btn.textContent = 'Copied!';
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = original;
        btn.disabled = false;
      }, 2000);
    }

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(done).catch(function () {
        fallbackCopy(text);
        done();
      });
    } else {
      fallbackCopy(text);
      done();
    }
  }

  function fallbackCopy(text) {
    var ta = document.createElement('textarea');
    ta.value = text;
    ta.setAttribute('readonly', '');
    ta.style.position = 'absolute';
    ta.style.left = '-9999px';
    document.body.appendChild(ta);
    ta.select();
    try { document.execCommand('copy'); } catch (e) { /* ignore */ }
    document.body.removeChild(ta);
  }

  /* ------------------------------------------------------------------ *
   * Smooth scroll for in-page TOC anchors
   * ------------------------------------------------------------------ */
  function initSmoothScroll() {
    var links = document.querySelectorAll('.bd-toc a[href^="#"], a.headerlink[href^="#"]');
    Array.prototype.forEach.call(links, function (link) {
      link.addEventListener('click', function (e) {
        var id = link.getAttribute('href').substring(1);
        var target = document.getElementById(id);
        if (target) {
          e.preventDefault();
          var headerH = document.querySelector('.site-header') ? 70 : 0;
          var y = target.getBoundingClientRect().top + window.pageYOffset - headerH - 12;
          window.scrollTo({ top: y, behavior: 'smooth' });
          history.replaceState(null, '', '#' + id);
        }
      });
    });
  }

  /* ------------------------------------------------------------------ *
   * Scroll progress bar
   * ------------------------------------------------------------------ */
  function initScrollProgress() {
    if (document.querySelector('.scroll-progress')) { return; }
    var bar = document.createElement('div');
    bar.className = 'scroll-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.appendChild(bar);

    var ticking = false;
    function update() {
      var max = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      var pct = max > 0 ? (window.pageYOffset / max) * 100 : 0;
      bar.style.width = pct + '%';
      ticking = false;
    }
    window.addEventListener('scroll', function () {
      if (!ticking) {
        window.requestAnimationFrame(update);
        ticking = true;
      }
    }, { passive: true });
    update();
  }

  /* ------------------------------------------------------------------ *
   * Apply highlight.js to all code blocks (local bundle already loaded)
   * ------------------------------------------------------------------ */
  function highlightCode() {
    if (typeof window.hljs !== 'undefined') {
      try {
        window.hljs.highlightAll();
      } catch (e) { /* no-op if highlighting impossible */ }
    }
  }

  /* ------------------------------------------------------------------ *
   * Mark the current page's sidebar link as active
   * ------------------------------------------------------------------ */
  function initActiveNavLink() {
    var path = window.location.pathname.replace(/\/$/, '') .split('/').pop() || 'index.html';
    var links = document.querySelectorAll('.bd-sidebar .sidebar-link');
    Array.prototype.forEach.call(links, function (link) {
      var href = link.getAttribute('href');
      if (href && href.split('/').pop() === path) {
        link.classList.add('active');
      }
    });
  }

  /* ------------------------------------------------------------------ *
   * Add a small language label chip to highlighted code blocks
   * ------------------------------------------------------------------ */
  function initLanguageLabels() {
    var pres = document.querySelectorAll('pre code[class*="language-"], pre code[class*="lang-"]');
    Array.prototype.forEach.call(pres, function (block) {
      if (block.closest('pre').querySelector('.lang-chip')) { return; }
      var cls = Array.prototype.slice.call(block.classList).find(function (c) {
        return c.indexOf('language-') === 0 || c.indexOf('lang-') === 0;
      });
      if (!cls) { return; }
      var lang = cls.replace(/^language-/, '').replace(/^lang-/, '').trim();
      if (!lang) { return; }
      var chip = document.createElement('span');
      chip.className = 'lang-chip';
      chip.textContent = lang;
      block.closest('pre').insertBefore(chip, block);
    });
  }

  /* ------------------------------------------------------------------ *
   * Client-side search over the build-generated search-index.json
   * ------------------------------------------------------------------ */
  var searchIndex = null;
  var searchIndexPromise = null;

  function loadSearchIndex() {
    if (searchIndex) { return Promise.resolve(searchIndex); }
    if (searchIndexPromise) { return searchIndexPromise; }
    searchIndexPromise = fetch('/search-index.json')
      .then(function (res) { return res.ok ? res.json() : []; })
      .then(function (data) {
        searchIndex = data || [];
        return searchIndex;
      })
      .catch(function () {
        searchIndex = [];
        return searchIndex;
      });
    return searchIndexPromise;
  }

  function scoreResult(item, terms) {
    var title = (item.title || '').toLowerCase();
    var text = (item.text || '').toLowerCase();
    var score = 0;
    terms.forEach(function (term) {
      if (title.indexOf(term) !== -1) { score += 10; }
      if (text.indexOf(term) !== -1) { score += 1; }
    });
    return score;
  }

  function renderResults(results, panel) {
    if (!results.length) {
      panel.innerHTML = '<div class="search-empty px-3 py-2 small">No matching pages.</div>';
      panel.hidden = false;
      return;
    }
    var html = results.map(function (r) {
      return '<a class="search-result" href="' + r.url + '">' +
               '<span class="search-result-title">' + escapeHtml(r.title) + '</span>' +
               '<span class="search-result-url">' + escapeHtml(r.url.replace(/\.html$/, '').replace(/^\.\//, '')) + '</span>' +
             '</a>';
    }).join('');
    panel.innerHTML = html;
    panel.hidden = false;
  }

  function escapeHtml(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
  }

  function initSearch() {
    var input = document.querySelector('.site-search');
    if (!input) { return; }
    var panel = input.closest('.search-wrap').querySelector('.search-results');

    input.addEventListener('input', function () {
      var q = input.value.trim();
      if (q.length < 2) {
        panel.hidden = true;
        return;
      }
      var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
      loadSearchIndex().then(function (index) {
        var results = index
          .map(function (item) { return { item: item, score: scoreResult(item, terms) }; })
          .filter(function (x) { return x.score > 0; })
          .sort(function (a, b) { return b.score - a.score; })
          .slice(0, 12)
          .map(function (x) { return x.item; });
        renderResults(results, panel);
      });
    });

    input.addEventListener('focus', function () {
      if (input.value.trim().length >= 2 && !panel.hidden) { panel.hidden = false; }
    });

    document.addEventListener('click', function (e) {
      if (!input.closest('.search-wrap').contains(e.target)) { panel.hidden = true; }
    });
  }

  /* eslint-disable-next-line no-unused-vars */
  var _unused = ready;
})();