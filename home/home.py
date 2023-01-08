from flask import Blueprint, jsonify

home = Blueprint('home', __name__, url_prefix='/home')

@home.get("/")
def new_home():
    return jsonify ({"message": "Hello World from the home route"}), 200
