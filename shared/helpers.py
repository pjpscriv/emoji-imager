import re
import random

from flask import make_response

HEX_RANGE = '0123456789ABCDEF'
HEX_COLOR_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'


def random_color() -> str:
    return "#"+''.join([random.choice(HEX_RANGE) for j in range(6)])


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

def chill_str(color: str) -> str:
  return color.lower().replace('#', '')