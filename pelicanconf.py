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

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20


THEME = 'themes/pelican-cait'

USE_CUSTOM_MENU = True
CUSTOM_MENUITEMS = (
    ('About', '/pages/about.html'),
)

DISPLAY_PAGES_ON_MENU = False

STATIC_PATHS = ['images', 'extra/CNAME', 'extra/robots.txt', 'javascripts']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        # 'mdx_linkify.mdx_linkify': {},
        'plugins.embed_github:EmbedGithubExtension': {},
        'sane_lists': {},
    },
    'output_format': 'html5',
}

MARKUP = ('md', )

from pelican_jupyter import liquid as nb_liquid
PLUGINS = [nb_liquid, "sitemap"]

IGNORE_FILES = [".ipynb_checkpoints"]


COOKIE_CONCENT = True

USE_OPEN_GRAPH = True

SITE_DESCRIPTION = 'そすすすすすすす'
OPEN_GRAPH_IMAGE = 'images/siteicon.png'

SITEMAP = {
    "exclude": ["tag/", "category/"],
    "format": "xml",
    "priorities": {
        "articles": 0.6,
        "indexes": 0.3,
        "pages": 0.3
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "daily",
        "pages": "daily"
    }
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True