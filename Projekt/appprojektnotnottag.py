# Przy pierwszym uruchomieniu:  flask --app app shell
# A następnie:
# >>> db.create_all()
# >>> exit()
#
# Dalej uruchamiamy: flask --app app app
import sqlalchemy
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://my_user:secret@127.0.0.1/my_database'
db = SQLAlchemy(app)


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    notename = db.Column(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Note %r>' % self.notename


def get_notes(session):
    return session.query(Note).all()


def create_note(name, session):
    try:
        note = Note(notename=name)
        session.add(note)
        session.commit()
    except sqlalchemy.exc.IntegrityError as e:
        print(e)
        session.rollback()
        return False
    else:
        return True

def remove_note(name, session):
    user = session.query(Note).filter_by(notename=name).one()
    session.delete(user)
    session.commit()

@app.route('/')
def hello():
    return render_template('formprojektnot.html', data=get_notes(db.session),
                           tytul="Notatki+", no_error=True)


@app.route('/add_note')
def add():
    args = request.args
    no_error = create_note(args["name"], db.session)
    if no_error:
        tytul = "Dodano notatkę"
    else:
        tytul = "Taka notatka już istnieje"

    return render_template('formprojektnot.html', data=get_notes(db.session),
                           no_error=no_error,
                           tytul=tytul)


@app.route('/remove_note')
def remove():
    args = request.args
    remove_note(args["values"], db.session)
    no_error = True
    if no_error:
        tytul = "Usunieto notatkę"
    return render_template('formprojektnot.html', data=get_notes(db.session),
                           no_error=no_error,
                           tytul=tytul)


# app laczy sie z form i pracuje z form z folderu sqlalchemy,
# jak sie wlaczy ktorekolwiek app.py trzeba znalexc do ktorego html sie odwoluje
# zawsze na początek trzeba zrobić bazę danych (na samej górze) robimy w teminalu
