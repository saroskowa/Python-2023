# flask --app app2 run
#
from flask import Flask, render_template, request

app = Flask(__name__)


data = []

@app.route('/')
def hello():
    return render_template('formzadanie.html', imie=" ")


@app.route('/add')
def add():
    args = request.args
    print(args)
    data.append(args["name"])

    return render_template('formzadanie.html', imie=args["name"])

# @app.route('/add')
# def add():
#     args = request.args
#     print(args)
#     imie = args["name"]
#     print(imie)
#     return render_template('imie.html', name=imie)