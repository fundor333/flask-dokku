#flask_app.py
from flask import Flask
from flask_dotenv import DotEnv

import os

app = Flask(__name__)
# https://github.com/grauwoelfchen/flask-dotenv
env = DotEnv(app)

@app.route("/")
def hello():
    return "GoodNight World!"

@app.route("/db_uri")
def config(key):
    return str(os.environ.get('DATABASE_URL'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
