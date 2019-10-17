from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
  return render_template("index.html")

@app.route('/character', methods=['GET', 'POST'])
def computeCharacter():
  if request.method == 'POST':
    userdata = dict(request.form)
    # print(userdata)
    character = ""
    return "You said " + str(userdata["book"]) + "!"
  else:
    return "Sorry, there was an error."
  


if __name__ == "__main__":
  app.run()
