from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import random 
import string

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
    bucket_id = db.Column(db.String(16), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def create_bucket_id(self):
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(16))
        main_id = self.query.filter_by(bucket_id=result_str).first()
        if main_id:
            pass
        else:
            return result_str


    def __init__(self, **kwargs):
        super().__init__(**kwargs) 
        self.bucket_id = self.create_bucket_id()

    def __repr__(self) -> str:
        return f'Bucket>>> {self.name}'