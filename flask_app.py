#flask_app.py
from flask import Flask
from flask_dotenv import DotEnv
from flask import render_template

import os

app = Flask(__name__)
# https://github.com/grauwoelfchen/flask-dotenv
env = DotEnv(app)

@app.route("/")
def hello():
    dict = {}
    dict['os_version'] = os.uname()
    return render_template("base.html", os_version=os.uname())

@app.route("/db_uri")
def config(key):
    return str(os.environ.get('DATABASE_URL'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
