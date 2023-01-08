from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() 


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(80), unique=False)
    email = db.Column(db.String(244), unique=True)
    password = db.Column(db.String(16), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate = datetime.now())
    buckets = db.relationship('Bucket', backref='user')

    def __repr__(self) -> str:
        return f'User>>> {self.username}'


class Bucket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    description = db.Column(db.String(244), nullable=False)
    image_link = db.Column(db.String(2048), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f'Bucket>>> {self.name}'