#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Anita Tran'
SITENAME = 'Anita Tran'
SITEDESCRIPTION = '"And now for something completely different.” – Monty Python'
SITEURL = 'https://anitatea.github.io/blog'

# plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['i18n_subsites', 'tipue_search']
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# theme and theme localization
THEME = '../pelican-fh5co-marble'
I18N_GETTEXT_LOCALEDIR = '../pelican-fh5co-marble/locale/'
I18N_GETTEXT_DOMAIN = 'messages'
I18N_GETTEXT_NEWSTYLE = True
TIMEZONE = 'America/Toronto'
DEFAULT_DATE_FORMAT = '%a, %d %b %Y'
I18N_TEMPLATES_LANG = 'en_US'
DEFAULT_LANG = 'en'
LOCALE = 'en_US'

# content paths
PATH = 'content'
PAGE_PATHS = ['pages/en']
ARTICLE_PATHS = ['blog']



# Post and Pages path
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# i18n
I18N_SUBSITES = {
  'de': {
    'PAGE_PATHS': ['pages/de'],
    'ARTICLE_PATHS': ['blog/de'],
    'LOCALE': 'de_DE'
  }
}

# logo path, needs to be stored in PATH Setting
LOGO = '../images/logo.png'

# special content
HERO = [
  {
    'image': './images/hero/patientlywaiting.png',
    # for multilanguage support, create a simple dict
    'title': {
      'en':'Patiently Waiting',
    },
    'text': {
      'en': 'Check emergency room wait times around Toronto by choosing a day: https://patientlywaiting.herokuapp.com/',
      'de': 'Jeglicher spezieller Inhalt den Sie hier bewerben möchten'
    },
    'links': [
      {
        # 'icon': 'icon-code',
        'icon':'fab fa-github fa-2x',
        'url': 'https://github.com/anitatea/patiently_waiting',
        'text': 'Github'
      }
    ]
  }, {
    'image': './images/hero/pokemon_go.png',
    # keep it a string if you dont need multiple languages
    'title': 'Pokemon Go - Prediction App',
    # keep it a string if you dont need multiple languages
    'text': 'A Pokémon predicting web-app bot based on one\'s IP location (latitude/longitude), weather, city, closeness to water and other geo-location features.',
    'links': [
      {
        # 'icon': 'icon-code',
        'icon':'fab fa-github fa-2x',
        'url': 'https://github.com/anitatea/pokemon_go',
        'text': 'Github'
      }
    ]
  }
]

# Social widget
SOCIAL = (
  ('Github', 'https://www.github.com/anitatea'),
  ('LinkedIn', 'https://www.linkedin.com/in/anitat/'),
  ('instagram', 'https://www.instagram.com/i.need.a.tea/'),
  ('email', 'anita.tran38@gmail.com')
)

ABOUT = {
  'image': './images/about/about.jpg',
  'mail': 'anita.tran38@gmail.com',
  # keep it a string if you dont need multiple languages
  'text': 'Drop a message!',
  'link': 'contact.html',
  # the address is also taken for google maps
  'address': 'Toronto, Canada',
  'github': 'https://github.com/anitatea/'
}

# navigation and homepage options
DISPLAY_PAGES_ON_MENU = True
DISPLAY_PAGES_ON_HOME = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
PAGE_ORDER_BY = 'order'

MENUITEMS = [
  ('Archive', 'archives.html'),
  ('Contact', 'contact.html')
]

DIRECT_TEMPLATES = [
  'index',
  'tags',
  'categories',
  'authors',
  'archives',
  'search', # needed for tipue_search plugin
  'contact' # needed for the contact form
]
#
# STATIC_PATHS = [
#     'images', 'extra/robots.txt', 'extra/favicon.ico'
#     ]
#
# EXTRA_PATH_METADATA = {
# #     'extra/custom.css': {'path': 'custom.css'},
#     'extra/robots.txt': {'path': 'robots.txt'},
#     'extra/favicon.ico': {'path': 'favicon.ico'}  # and this
# #    'extra/CNAME': {'path': 'CNAME'}
# #    'extra/LICENSE': {'path': 'LICENSE'},
# #    'extra/README': {'path': 'README'},
# }

# setup disqus
DISQUS_SHORTNAME = 'gitcd-dev'
DISQUS_ON_PAGES = False # if true its just displayed on every static page, like this you can still enable it per page

# setup google maps
GOOGLE_MAPS_KEY = 'AIzaSyCefOgb1ZWqYtj7raVSmN4PL2WkTrc-KyA'

#google tracking idea
GOOGLE_TRACKING_ID = "G-Q5LN56BLH8"
