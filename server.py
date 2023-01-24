from flask import Flask 
from home.home import home
from user.user import user
from buckets.bucket import bucket
from database import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test'

db.app = app
db.init_app(app)

migrate = Migrate(app, db, render_as_batch=True)


app.register_blueprint(home)
app.register_blueprint(user)
app.register_blueprint(bucket)
JWTManager(app)


if __name__ == "__main__":
    app.run(debug=True)