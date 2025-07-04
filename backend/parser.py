import os
import csv
from PIL import Image

from shared.types import Emoji, Emoji2
from shared.helpers import random_color, random_emoji, valid_emoji, read_emoji_data_file

SIZE = 350
OUT_DIR = '_out'
EMOJI_FILE = './backend/data/full_emoji.csv'
EMOJI_FILE_2 = './shared/emojis.csv'


''' Load all emojis and return them as an object list '''
def load_emojis() -> dict:
    emojis = {}
    with open(EMOJI_FILE, encoding='utf-8') as file:
        reader = csv.reader(file)
        reader.__next__()
        for row in reader:
            emoji = Emoji(row)
            emojis[emoji.emoji] = emoji
    return emojis

def load_emojis_2() -> dict:
    data = read_emoji_data_file(EMOJI_FILE_2)
    emojis = {}
    for emoji in [Emoji2(row) for row in data]:
        if not emoji.ignore:
            emojis[emoji.emoji] = emoji
    return emojis

EMOJI_DICT = load_emojis_2()
EMOJI_LIST = list(EMOJI_DICT.keys())


''' Generate a vertical gradient PIL Image '''
def generate_gradient(colour1: str, colour2: str, width: int, height: int) -> Image:
    base = Image.new('RGB', (width, height), colour1)
    top = Image.new('RGB', (width, height), colour2)
    mask = Image.new('L', (width, height))
    mask_data = []
    for y in range(height):
        mask_data.extend([int(255 * (y / height))] * width)
    mask.putdata(mask_data)
    base.paste(top, (0, 0), mask)
    return base


''' Take two images and combine them '''
def merge_images(foreground: Image, background: Image) -> Image:
    foreground = foreground.convert('RGBA')
    background = background.convert('RGBA')

    x = (background.size[0] - foreground.size[0]) // 2
    y = (background.size[1] - foreground.size[1]) // 2

    foreground_scaled = Image.new("RGBA", background.size)
    foreground_scaled.paste(foreground, (x, y))

    background = Image.alpha_composite(background, foreground_scaled)

    return background

'''Take unicode emoji and return the emoji object'''
def get_emoji(emoji_str: str) -> Emoji2:
    if emoji_str == '':
      emoji = None
    elif emoji_str and valid_emoji(emoji_str, EMOJI_LIST):
        emoji = EMOJI_DICT.get(emoji_str)
    else:
        emoji = random_emoji(EMOJI_DICT, EMOJI_LIST)
    return emoji
  

''' The juice. This is the main thing we want the API to do. '''
def generate_image(start: str, end: str, emoji: Emoji2, vendor: str) -> Image:
    gradient = generate_gradient(start, end, SIZE, SIZE)
    emoji_image = generate_emoji_image(emoji, vendor)
    return merge_images(emoji_image, gradient)


''' Take an emoji object and return the PIL image of it '''
def generate_emoji_image(emoji: Emoji2, vendor: str) -> Image:
    size = 160
    return emoji.get_image(vendor, size) if emoji else Image.new("RGBA", (size, size))


''' Return a gradient between two random colors '''
def random_gradient():
    s = random_color()
    e = random_color()
    return generate_gradient(e, s, SIZE, SIZE)


''' Create files of all the emojis with gradient backgrounds '''
def draw_all_emoji():
    try:
        os.mkdir(OUT_DIR)
    except:
        pass

    for emoji in EMOJI_DICT.values():
        emo_img = emoji.get_image()
        merged = merge_images(emo_img, random_gradient())
        merged.save(f'{OUT_DIR}/{emoji.id}-{emoji.name}.png')

