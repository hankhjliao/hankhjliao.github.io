#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Hank Liao'
SITENAME = u'Hank\'s Blog'
# SITESUBTITLE = 'A personal blog.'
SITEURL = ''
LOGO_IMG = 'https://github.com/identicons/hankliao87.png'
THEME = 'theme'
PATH = 'content'

MENUITEMS = (
    # ('Home', '/'),
    # ('About', '/about.html'),
    # ('Blog', '/blog/'),
)

DEFAULT_PAGINATION = 5
SUMMARY_MAX_LENGTH = 20

DEFAULT_LANG = 'en'
TIMEZONE = 'Asia/Taipei'
DATE_FORMATS = {
    'en': ('%Y/%m/%d'),
}

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.loopcontrols']}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# path-specific metadata
EXTRA_PATH_METADATA = {}

# static paths will be copied without parsing their contents
STATIC_PATHS = ['images']

DIRECT_TEMPLATES = ['index', 'tags',
                    'categories', 'authors', 'archives', 'search']

DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = False

ARTICLE_PATHS = ['articles']
ARTICLE_EXCLUDES = []
ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'
ARTICLE_ORDER_BY = 'reversed-date'

DISPLAY_PAGES_ON_MENU = False
PAGE_PATHS = ['pages']
PAGE_EXCLUDES = []
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

DRAFT_URL = 'posts/draft/{slug}/'
DRAFT_SAVE_AS = 'posts/draft/{slug}/index.html'

#UTTERANC_REPO_NAME = 'hankliao87/blog'
GISCUS_REPO_NAME = 'hankliao87/blog'
GISCUS_REPO_ID = 'MDEwOlJlcG9zaXRvcnkyMjI3Njc0OTU'
GISCUS_CATEGORY_ID = 'DIC_kwDODUcph84CAJSe'

################################
# Feed
################################

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

################################
# Links
################################

HOME_URL = 'https://hankliao87.github.io/'
GITHUB_URL = 'https://github.com/hankliao87/'
TWITTER_URL = 'https://twitter.com/hankliao87/'
# FACEBOOK_URL = '/'

# Blogroll
LINKS = ()

# Social widget
SOCIAL = ()

################################
# PLUGIN
################################

PLUGIN_PATHS = ['plugins']
PLUGINS = ["render_math", "tag_cloud", "better_codeblock_line_numbering",
           "pelican-encrypt-content", "tipue_search", "pelican-toc", "readtime"]

MARKDOWN = {
    'extensions': [
        'markdown.extensions.admonition',
        'markdown.extensions.codehilite',
        'markdown.extensions.extra',
        'markdown.extensions.nl2br',
        'mdx_include',
        'pymdownx.emoji',
        'pymdownx.inlinehilite',
        'pymdownx.keys',
        'pymdownx.magiclink',
        'pymdownx.mark',
        'pymdownx.tabbed',
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight', 'linenums': 'False'},
        "pymdownx.emoji": {"options": {"attributes": {"align": "absmiddle", "height": "20px", "width": "20px"}, }},
    },
}

TAG_CLOUD_STEPS = 4
TAG_CLOUD_SIDEBAR_MAX_ITEMS = 15
TAG_CLOUD_SORTING = "size"
TAG_CLOUD_BADGE = True

TIPUE_SEARCH = True

TOC = {
    'TOC_HEADERS': '^h[1-4]',
    'TOC_RUN': 'true',
    'TOC_INCLUDE_TITLE': 'false',
}
