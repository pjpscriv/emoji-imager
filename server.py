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
  if request.method == 'POST':
    userdata = dict(request.form)
    book = userdata["book"][0]
    character = model.compute_character(book)
    return "You're " + character + "!"
  else:
    return "Sorry, there was an error."
  
if __name__ == "__main__":
  app.run()
