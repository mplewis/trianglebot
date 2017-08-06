import re
from os import environ

# URL to the Groupme API endpoint
API_URL = 'https://api.groupme.com/v3/bots/post'

# URL to the Google Sheets JSON API endpoint
SHEET_BASE_URL = ('https://spreadsheets.google.com/feeds/cells/%s/%s'
                  '/public/values?alt=json')

SHEET_ID_MATCHER = r'spreadsheets\/d\/(.+)\/'

# Set by Heroku variables
COMMAND_PREFIX = environ['BOT_NAME'] + ' '
BOT_ID = environ['GROUPME_BOT_ID']
WORKSHEET_KEYS_TO_SCRAPE = environ['WORKSHEET_KEYS'].split(',')
INDEX_REDIRECT_URL = 'https://github.com/mplewis/trianglebot'
SHEET_KEY = re.search(SHEET_ID_MATCHER, environ['DOCUMENT_URL']).group(1)
