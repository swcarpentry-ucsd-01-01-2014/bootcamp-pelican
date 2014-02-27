#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Software Carpentry'
SITENAME = u'Software Carpentry'
SITEURL = ''

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

PAGE_DIR = 'lessons'
ARTICLE_DIR = 'news'
THEME = 'themes/pelican-elegant'
PAGE_SAVE_AS = '{category}/{slug}.html'
PAGE_URL = PAGE_SAVE_AS
ARTICLE_SAVE_AS = 'news/{slug}.html'
ARTICLE_URL = ARTICLE_SAVE_AS
DISPLAY_PAGES_ON_MENU = False
PLUGIN_PATH = 'pelican-plugins'

PLUGINS = ['sitemap', 'extract_toc', 'tipue_search']
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc', 'fenced_code']
DIRECT_TEMPLATES = (('tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
TAG_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

SOCIAL = (
        ('Twitter', 'http://twitter.com/swcarpentry'),
        ('Github', 'http://github.com/swcarpentry'),
        #('GitTip', 'http://gittip.com/swcarpentry'),
        ('Email', 'mailto:'),
          )

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
