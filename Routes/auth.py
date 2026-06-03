from flask import Blueprint, request, jsonify
from APITest.routes.extensions import db, bcrypt
from models.user import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/")
def home():
    return jsonify({"message": "API is running"})

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    hashed = bcrypt.generate_password_hash(
        data["password"]
    ).decode("utf-8")

    user = User(username=data["username"], password=hashed)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User created"})


@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if user and bcrypt.check_password_hash(user.password, data["password"]):
        return jsonify({"message": "Login success"})

    return jsonify({"message": "Invalid credentials"}), 401