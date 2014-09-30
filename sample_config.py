# URL to the Groupme API endpoint
API_URL = 'https://api.groupme.com/v3/bots/post'

# URL to the Google Sheets JSON API endpoint
SHEET_BASE_URL = ('https://spreadsheets.google.com/feeds/cells/%s/%s'
                  '/public/values?alt=json')

# Prefix searches with this string. Trailing space is important!
COMMAND_PREFIX = 'cortana '
# Your bot's ID. Get this at https://dev.groupme.com/bots
BOT_ID = '9693ddf3f1604e81ffb9acb8cb'
# Your Google Sheet key. You can find this in the URL: key=YOUR_KEY_HERE
SHEET_KEY = '0Ap_Q66-EH4RtdER3VVUwQUs4UmwyNXJtYWNGLUxJYVE'

# Give your worksheets' ugly keys pretty names
WORKSHEET_KEYS = {'actives': 'od6', 'pledges': 'od4', 'boarders': 'od7'}
# Pick which worksheets to include in your "database"
WORKSHEETS_TO_SCRAPE = ['actives', 'pledges']
# Leave this as is. It picks the keys from your list of pretty sheet names.
WORKSHEET_KEYS_TO_SCRAPE = [WORKSHEET_KEYS[w]
                            for w in WORKSHEETS_TO_SCRAPE]
