# flask --app hello run

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# flask --app hello run w terminalu to wyskuje 5000
# (venv) PS C:\Users\localadmin\PycharmProjects\Python-2023\19_Flask-aplikacje_webowe\minimal> cd ..\minimal\
# (venv) PS C:\Users\localadmin\PycharmProjects\Python-2023\19_Flask-aplikacje_webowe\minimal> python hello2_run.py
# to wyskakuje 8000