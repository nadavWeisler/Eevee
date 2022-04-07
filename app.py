from flask import Flask, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

import __data__ as data

app = Flask(data.__app_name__)

app.config['SQLALCHEMY_DATABASE_URI'] = data.__db_uri__

db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(80), unique=True, nullable=False, primary_key=True)
    password = db.Column(db.String(80), nullable=False)
    trello_key = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method != "GET":
        return send_from_directory('templates', 'index.html')
    else:
        name = request.form.get("name")
        email = request.values.get("email")
        trello1 = request.values.get("trello1")
        trello2 = request.values.get("trello2")
        trello3 = request.values.get("trello3")
        moodleUserName = request.values.get("moodleUserName")
        moodlePassword = request.values.get("moodlePassword")
        print(name, email, trello1, trello2, trello3,
              moodleUserName, moodlePassword)
        admin = User(username='admin', password="df", trello_key="dfd", email='admin@example.com')
        guest = User(username='guest', email='guest@example.com', password="df", trello_key="sdgsdf")
        db.session.add(admin)
        db.session.add(guest)
        db.session.commit()
        return send_from_directory('templates', 'thankYou.html')


@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder, 'favicon.ico', mimetype='image/vnd.microsoft.icon')
