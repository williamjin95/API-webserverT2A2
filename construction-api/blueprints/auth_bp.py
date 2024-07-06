from flask import request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models.user import User
from app import db
from schema import user_schema

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = User(**data)
    db.session.add(user)
    db.session.commit()
    return user_schema.jsonify(user), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user is None or user.password != data['password']:
        return jsonify({"msg": "Invalid username or password"}), 401
    access_token = create_access_token(identity=user.username)
    return jsonify(access_token=access_token)

@auth_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
