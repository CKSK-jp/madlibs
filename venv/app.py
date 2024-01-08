from flask import Flask, request, render_template
from random import randint, choice

app = Flask(__name__)

questions = {"plural_noun": "", "verb": ""}


@app.route("/")
def open_home():
    return render_template("home.html")
