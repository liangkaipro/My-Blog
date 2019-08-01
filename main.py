# encoding: utf-8
from flask import Flask
from config import DevCofig

app = Flask(__name__)
app.config.from_object(DevCofig)


@app.route('/')
def home():
    return 'hello world'


if __name__ == '__main__':
    app.run()