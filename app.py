from random import choice, randint

from flask import Flask, render_template, request

app = Flask(__name__)

questions = {"plural_noun": "", "verb": ""}


@app.route("/")
def open_home():
    return render_template("home.html")
