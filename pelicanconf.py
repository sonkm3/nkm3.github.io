#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import datetime

AUTHOR = 'sonkmr'
SITENAME = 'nkm3'
SITEURL = 'https://nkm3.org'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
CURRENT_YEAR = datetime.datetime.now().year


# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/pelican-cait'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    ('About', '/pages/about.html'),
)



DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'mdx_linkify.mdx_linkify': {},
    },
    'output_format': 'html5',
}

MARKUP = ('md', )

from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid]

IGNORE_FILES = [".ipynb_checkpoints"]

GOOGLE_ANALYTICS = 'UA-1928342-2'
