import io
from PIL import Image
from flask import Flask, render_template_string, request

from shared.helpers import *
from backend.parser import generate_image


app = Flask(__name__)


''' The image endpoint. This is the one that does the heavy lifting '''
@app.route('/image', methods=['GET'])
def get_image():
    s = '#' + request.args.get('start')
    e = '#' + request.args.get('end')
    em = request.args.get('emoji')

    print(f'REQUEST: ({s}->{e} / {em})')

    gradient_start = s if valid_color(s) else random_color()
    gradient_end = e if valid_color(e) else random_color()
    emoji = em if em else None
    image = generate_image(gradient_start, gradient_end, emoji)

    byte_buffer = io.BytesIO()
    image.save(byte_buffer, format='PNG')
    img_str = byte_buffer.getvalue()

    return image_response(img_str)


''' Basically just a template wrapper around the image endpoint '''
@app.route('/<start>/<end>/<emoji>', methods=['GET'])
def image_html(start, end, emoji):
    return render_template_string(f'<img src="/image?start={start}&end={end}&emoji={emoji}">')


''' The root. Surely just template a random image here right? '''
@app.route('/',  methods=['GET'])
def root():
    return render_template_string('<p>Well there ain\'t nothin\' here.</p> <p><a href="/random/random/random">Click here</a> to see a random emoji.</p>')


''' Catchallllll WHOOP '''
@app.route('/<anything_else>',  methods=['GET'])
def fallback(anything_else):
    return 'Well that ain\'t nothing lad'



if __name__ == '__main__':
    app.run()

