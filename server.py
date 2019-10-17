from flask import Flask
from flask import render_template
from flask import request
import model


app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html")

@app.route('/result', methods=['GET', 'POST'])
def result():
  if request.method == 'POST' and len(dict(request.form)) > 0:
    userdata = dict(request.form)
    book = userdata["book"][0]
    character = model.get_character(book)
    gif_url = model.get_gif(character)
    return render_template("result.html", character=character, gif_url=gif_url)
  else:
    return "Sorry, there was an error."
  
if __name__ == "__main__":
  app.run()
