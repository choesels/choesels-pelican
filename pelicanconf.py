AUTHOR = 'ulf.gj'
SITENAME = 'The Choesels'
# SITEURL = "https://choesels.github.io"
SITEURL = ''

PATH = "content"
TIMEZONE = 'Europe/Brussels'
DEFAULT_LANG = 'en'

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "theme"
STYLESHEET_URL = True

# TWITTER_USERNAME =

# Blogroll
LINKS = (
    ("Youtube", "https://www.youtube.com/@ChristopheDarc/"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


####   my misc variables and logic   ####

CONCERTS = [
    {"title": "Summer Fest 1998", "date": "1998-06-20", "location": "Central Park, NYC, USA"},
    {"title": "Bar Mitzva for Ezekiel 1", "date": "2003-03-01", "location": "Sablon, Bxl"},
    {"title": "Bar Mitzva for Ezekiel 2", "date": "2003-03-01", "location": "Sablon, Bxl"},
    {"title": "Bar Mitzva for Ezekiel 3", "date": "2003-03-01", "location": "Sablon, Bxl"},
    {"title": "Autumn Jam", "date": "2004-10-05", "location": "Downtown Hall, Uptown"},
    {"title": "", "date": "2024-03-23", "location": "Cafe Terminus, Evere"},
    {"title": "", "date": "2024-05-04", "location": "Le Fille de on Pere, Rebecq"},
    {"title": "CANCELLED", "date": "2024-06-22", "location": "??"},
    {"title": "", "date": "2024-07-27", "location": "l'Exelcior, Jette"},
    {"title": "", "date": "2024-09-14", "location": "Madras Bar, Braine-l'Alleud"},
    {"title": "", "date": "2024-09-28", "location": "Cafe Terminus, Evere"},
    {"title": "", "date": "2024-12-21", "location": "Le Métropole, Braine-l'Alleud"},
    {"title": "Bar Mitzva for Ezekiel 1", "date": "2028-02-01", "location": "Sablon, Bxl"},
    {"title": "Bar with Beers for Ezekiel 2", "date": "2028-03-01", "location": "Sablon, Bxl"},
    {"title": "Barbapapa for Kids", "date": "2028-04-01", "location": "Sablon, Bxl"},
    {"title": "Bar for Me", "date": "2029-01-01", "location": "Sablon, Bxl"},
]

from datetime import datetime, date

def as_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()

JINJA_FILTERS = {
    'as_date': as_date,
}

JINJA_GLOBALS = {
    'concerts': CONCERTS,
    'date': date,
}

