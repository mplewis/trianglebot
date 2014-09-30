#!/usr/bin/env python3

import config

import requests
from fuzzywuzzy import fuzz


def json_to_cell_matrix(data):
    cells = data['feed']['entry']
    rows = max([int(cell['gs$cell']['row']) for cell in cells])
    cols = max([int(cell['gs$cell']['col']) for cell in cells])
    sheet = [['(none)' for i in range(cols)] for j in range(rows)]
    for cell in cells:
        row = int(cell['gs$cell']['row']) - 1
        col = int(cell['gs$cell']['col']) - 1
        sheet[row][col] = cell['gs$cell']['$t'].strip()
    return sheet


def rows_from_cell_matrix(sheet):
    col_titles = sheet[0]
    raw_rows = sheet[1:]
    rows = []
    for row in raw_rows:
        row_data = {}
        first_name = ''
        last_name = ''
        for col, cell in enumerate(row):
            col_title = col_titles[col]
            col_title_lower = col_title.lower()
            if 'name' in col_title_lower:
                if 'first' in col_title_lower:
                    first_name = cell
                elif 'last' in col_title_lower:
                    last_name = cell
            else:
                row_data[col_title] = cell
        name = ('%s %s' % (first_name, last_name)).strip()
        row_data['Name'] = name
        rows.append(row_data)
    return rows


def search_for_name(rows, name):
    best_score = 0
    best_row = None
    if not rows:
        return (best_row, best_score)
    for row in rows:
        score = fuzz.partial_ratio(name.lower(), row['Name'].lower())
        if score > best_score:
            best_row = row
            best_score = score
    return (best_row, best_score)


def kv_to_str(key, value):
    return '%s: %s' % (key, value)


def row_summary(row, priority_keys=[], excluded_keys=[]):
    row_pairs = []
    for key in priority_keys:
        if key in row:
            row_pairs.append((key, row[key]))
    for key in row:
        if key not in priority_keys and key not in excluded_keys:
            row_pairs.append((key, row[key]))
    row_strings = [kv_to_str(*pair) for pair in row_pairs]
    summary = ', '.join(row_strings)
    return summary


def summary_for_name(rows, name):
    PRIORITY_KEYS = ['Cell Phone', 'Email']
    EXCLUDED_KEYS = ['Triangle Email', 'Name']
    row, score = search_for_name(rows, name)
    if not row:
        return None
    summary = row_summary(row, priority_keys=PRIORITY_KEYS,
                          excluded_keys=EXCLUDED_KEYS)
    return '%s%% match: %s, ' % (score, row['Name']) + summary


def worksheet_keys_to_rows(keys):
    rows = []
    for worksheet_key in keys:
        SHEET_URL = (config.SHEET_BASE_URL %
                     (config.SHEET_KEY, worksheet_key))
        data = requests.get(SHEET_URL).json()
        cells = json_to_cell_matrix(data)
        partial_rows = rows_from_cell_matrix(cells)
        rows += partial_rows
    return rows
