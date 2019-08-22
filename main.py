# encoding: utf-8
from flask import Flask
from config import DevCofig
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(DevCofig)
db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'hello world'


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    def __init__(self, username):
        self.username = username

    def __repr__(self):
        return "<User '{}'>".format(self.username)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime())
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'))


if __name__ == '__main__':
    app.run()
