from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from models.hour import Hour
from app import db
from schema import hour_schema, hours_schema

hours_bp = Blueprint('hours', __name__)

@hours_bp.route('/', methods=['POST'])
@jwt_required()
def add_hour():
    data = request.get_json()
    errors = hour_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    hour = Hour(**data)
    db.session.add(hour)
    db.session.commit()
    return hour_schema.jsonify(hour), 201

@hours_bp.route('/', methods=['GET'])
def get_hours():
    hours = Hour.query.all()
    return hours_schema.jsonify(hours), 200

@hours_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_hour(id):
    hour = Hour.query.get_or_404(id)
    data = request.get_json()
    errors = hour_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items():
        setattr(hour, key, value)
    db.session.commit()
    return hour_schema.jsonify(hour), 200

@hours_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_hour(id):
    hour = Hour.query.get_or_404(id)
    db.session.delete(hour)
    db.session.commit()
    return '', 204
