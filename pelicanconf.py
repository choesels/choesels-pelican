from datetime import datetime, date
import os
import re


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

PAGE_PATHS = ['pages']

CONCERTS = [
    {"title": "Summer Fest 1998", "date": "1998-06-20", "location": "Central Park, NYC, USA", "event_link": ""},
    {"title": "Bar Mitzva for Ezekiel 1", "date": "2003-03-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Bar Mitzva for Ezekiel 2", "date": "2003-03-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Bar Mitzva for Ezekiel 3", "date": "2003-03-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Autumn Jam", "date": "2004-10-05", "location": "Downtown Hall, Uptown", "event_link": ""},
    {"title": "", "date": "2024-03-23", "location": "Le Terminus, Evere", "event_link": "https://www.facebook.com/events/8-rue-%C3%A9glise-st-pierre-jette-belgique/the-choesels/457359800386869/"},
    {"title": "", "date": "2024-05-04", "location": "La Fille de son Père, Rebecq", "event_link": ""},
    {"title": "CANCELLED", "date": "2024-06-22", "location": "??", "event_link": ""},
    {"title": "", "date": "2024-07-27", "location": "l'Exelcior, Jette", "event_link": ""},
    {"title": "", "date": "2024-09-14", "location": "Madras Bar, Braine-l'Alleud", "event_link": "https://example.com", "bajs": "korv"},
    {"title": "", "date": "2024-09-28", "location": "Le Terminus, Evere", "event_link": ""},
    {"title": "", "date": "2024-12-21", "location": "Le Métropole, Braine-l'Alleud", "event_link": ""},
    {"title": "Bar Mitzva for Ezekiel 1", "date": "2028-02-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Bar with Beers for Ezekiel 2", "date": "2028-03-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Barbapapa for Kids", "date": "2028-04-01", "location": "Sablon, Bxl", "event_link": ""},
    {"title": "Bar for Me", "date": "2029-01-01", "location": "Sablon, Bxl", "event_link": "#"},
]


def as_date(value):
    return datetime.strptime(value, "%Y-%m-%d").date()

""" Display latest poster in concert section """
# poster image path
folder = 'theme/static/img/posters'
# Regex to extract date in format YYYY-MM-DD (e.g., 2028-01-01)
date_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')
latest_file = None
latest_date = None
for filename in os.listdir(folder):
    match = date_pattern.search(filename)
    if match:
        # Parse the date from filename
        file_date = datetime.strptime(match.group(1), "%Y-%m-%d")
        # Compare to current latest
        if latest_date is None or file_date > latest_date:
            latest_date = file_date
            latest_file = filename


""" Misc variable exports for use in templates """
JINJA_FILTERS = {
    'as_date': as_date,
}
JINJA_GLOBALS = {
    'concerts': CONCERTS,
    'date': date,
    'latest_poster': latest_file,
    'latest_poster_date': latest_date.date(),
}