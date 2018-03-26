#flask_app.py
from flask import Flask
from flask_dotenv import DotEnv
import platform

import os

app = Flask(__name__)
# https://github.com/grauwoelfchen/flask-dotenv
env = DotEnv(app)

@app.route("/")
def hello():
    return f"<head><title> goodnight world by flask and dokku</title></head>"
        f"<h1>Goodnight World!</h1>"
        f"from {os.uname()} "

@app.route("/db_uri")
def config(key):
    return str(os.environ.get('DATABASE_URL'))

if __name__ == "__main__":
    app.run(host="0.0.0.0")
