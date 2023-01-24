from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token
from werkzeug.security import generate_password_hash, check_password_hash
from database import User, db
import validators

user = Blueprint("user", __name__, url_prefix="/users")

@user.get("/")
def get_all_users():
    all_users = User.query.all()
    data = []
    for user in all_users:
        data.append({
            "id": user.id,
            "username": user.username,
            "email": user.email 
        })
    return data

@user.post("/register")
def register_user():
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('password')

    if not validators.email(email): 
        return jsonify({"error": "invalid email"}), 400
    
    if User.query.filter_by(email=email).first() is not None:
        return jsonify({"error": "someone with this email already exists"}), 400
    
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"error": "somone with this username already exists"}), 400

    password_hash = generate_password_hash(password)
    user = User(username=username, password=password_hash, email=email)
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "username": username,
        "email": email,
    }), 201 

@user.post("/login")
def login():
    email = request.json.get("email", '')
    password = request.json.get("password", '')

    user = User.query.filter_by(email=email).first()
    if user:
        password_check = check_password_hash(user.password, password)
        if password_check:
            refresh_token = create_refresh_token(identity=user.id)
            access_token = create_access_token(identity=user.id)

            return jsonify({
                "refresh-token": refresh_token,
                "access-token": access_token
            })
    return jsonify({"error": "Incorrect Credentials"}), 400
