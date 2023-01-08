from flask import Blueprint
from database import User

user = Blueprint("user", __name__, url_prefix="/users")

@user.get("/")
def get_all_users():
    all_users = User.query.all()
    return {"all_users": all_users}


