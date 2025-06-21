import re
import csv
import random

from flask import make_response

HEX_RANGE = '0123456789ABCDEF'
HEX_COLOR_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
COLORS = [
    '#defcf4',
    '#f8dcd8',
    '#e9daf7',
    '#fef0d3',
    '#dff4f9',
    '#fddeed',
    '#dcf3df',
    '#fee4d3',
]
VENDOR_LIST = [
    'apple',
    'microsoft',
    'google',
    'twitter'
]

def random_color(exclude: str = '') -> str:
    return random.choice([color for color in COLORS if color != exclude.lower()])


def valid_color(input_string: str) -> bool:
    regexp = re.compile(HEX_COLOR_REGEX)
    return regexp.search(input_string)


def random_emoji(emoji_dict: dict, emoji_list: list):
    i = random.randrange(len(emoji_dict))
    return emoji_dict.get(emoji_list[i])


def valid_emoji(emoji: str, emoji_list: list) -> bool:
    return emoji in emoji_list


def image_response(img_str, filename):
    resp = make_response(img_str, 200)
    resp.headers.set('Content-Type', 'image/png')
    resp.headers.set('Content-Disposition', 'attachment', filename=filename)
    return resp


def chill_str(string: str) -> str:
  string = string.lower().replace(' ', '_')
  return ''.join([c for c in string if c.isalnum() or c == '_'])


def read_emoji_data_file(file_path):
    headers = [ 'emoji', 'name', 'group', 'sub_group', 'codepoints', 'name_override', 'ignore' ]
    data = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, fieldnames=headers)
        next(reader)
        data = [row for row in reader]
    return data


def get_row_filename(row: dict) -> str:
    name = row.get('name', '')
    override = row.get('name_override', '')
    name = override if override != '' else name
    
    name = name.lower()
    name = name.replace(';', '')
    name = name.replace(':', '')
    name = name.replace('’', '')
    name = name.replace('(', '')
    name = name.replace(')', '')
    name = name.replace('!', '')
    name = name.replace('“', '')
    name = name.replace('”', '')
    name = name.replace(',', '')
    name = name.replace('.', '')
    name = name.replace('ñ', 'n')
    name = name.replace('ç', 'c')
    name = name.replace('é', 'e')
    name = name.replace('ã', 'a')
    name = name.replace('í', 'i')
    name = name.replace('å', 'a')
    name = name.replace('ô', 'o')
    name = name.replace('& ', '')
    name = name.replace('- ', '')
    name = name.replace(' ', '-')

    codepoints = row['codepoints'].replace(' ', '-').lower()
    if codepoints.startswith('00'):
        codepoints = codepoints[2:]
    
    return f"{name}_{codepoints}.png"
