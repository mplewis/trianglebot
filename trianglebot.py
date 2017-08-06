#!/usr/bin/env python3

import config
import sheets_api

import requests
from flask import Flask, request, redirect

import json


app = Flask(__name__)


def send_to_group(message):
    headers = {'content-type': 'application/json; charset=utf-8'}
    to_api = json.dumps({'bot_id': config.BOT_ID, 'text': message})
    requests.post(config.API_URL, to_api, headers=headers)


def summary_for_name(name):
    rows = sheets_api.worksheet_keys_to_rows(config.WORKSHEET_KEYS_TO_SCRAPE)
    summary = sheets_api.summary_for_name(rows, name)
    return summary or 'Sorry, no match found for "%s".' % name


@app.route('/', methods=['POST'])
def posted():
    data = request.get_json()
    text = data['text']
    clean = text.lower().strip()
    if not clean.startswith(config.COMMAND_PREFIX.lower()):
        print('Ignored:  ', repr(text))
        return ''
    split_point = len(config.COMMAND_PREFIX)
    query = text[split_point:].strip()
    print('Searching:', repr(query))
    message = 'Searching for "%s"...' % query
    send_to_group(message)
    send_to_group(summary_for_name(query))
    return ''


@app.route('/', methods=['GET'])
def about_me():
    return redirect(config.INDEX_REDIRECT_URL)


if __name__ == '__main__':
    app.run(debug=True)
