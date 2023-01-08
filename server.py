from flask import Flask 
from home.home import home
from user.user import user
from database import db
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_sqlite.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'test'

db.app = app
db.init_app(app)

migrate = Migrate(app, db)


app.register_blueprint(home)
app.register_blueprint(user)


if __name__ == "__main__":
    app.run(debug=True)