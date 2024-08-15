from flask import (
  Flask,
  request,
  redirect
)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/redirect-me")
def redirect_me():
  return redirect(request.args.get("url"))
