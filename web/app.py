from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cascontrol.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

with app.app_context():
    db = SQLAlchemy(app)
    db.create_all()

@app.get('/')
def home():
    return 'Hello, World!'

class settings(db.Model):
    '''Settings table, stores all settings for the application'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    value = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<settings %r>' % self.name