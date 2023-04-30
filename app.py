import io
from PIL import Image
from flask import Flask, render_template_string, request, render_template

from shared.helpers import *
from backend.parser import get_emoji, generate_image


app = Flask(__name__)



''' The image endpoint. This is the one that does the heavy lifting '''
@app.route('/image', methods=['GET'])
def get_image():
    s = '#' + request.args.get('start', 'invalid')
    e = '#' + request.args.get('end', 'invalid')
    em = request.args.get('emoji', None)

    print(f'REQUEST: ({s}->{e} / {em})')

    gradient_start = s if valid_color(s) else random_color()
    gradient_end = e if valid_color(e) else random_color()
    emoji = get_emoji(em) if em else None
    print(f'EMOJI: {chill_str(emoji.name) if emoji else "empty"}')
    image = generate_image(gradient_start, gradient_end, emoji)
    filename = (chill_str(emoji.name) + '_' if emoji else '') + f'{chill_str(gradient_start)}_{chill_str(gradient_end)}.png'

    byte_buffer = io.BytesIO()
    image.save(byte_buffer, format='PNG')
    img_str = byte_buffer.getvalue()

    return image_response(img_str, filename)


''' Basically just a template wrapper around the image endpoint '''
@app.route('/<start>/<end>/<emoji>', methods=['GET'])
def image_html(start, end, emoji):
    return render_template('result.html', start=start, end=end, emoji=emoji)


''' The root. Surely just template a random image here right? '''
@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


''' Catchallllll WHOOP '''
@app.route('/<anything_else>',  methods=['GET'])
def fallback(anything_else):
    return 'Well that ain\'t nothing lad'



if __name__ == '__main__':
    app.run()

