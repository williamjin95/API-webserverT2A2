from flask import request, jsonify, Blueprint
from models.location import Location
from app import db
from schema import location_schema, locations_schema
from flask_jwt_extended import jwt_required

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('/', methods=['POST'])
@jwt_required()
def add_location():
    data = request.get_json()
    errors = location_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    location = Location(**data)
    db.session.add(location)
    db.session.commit()
    return location_schema.jsonify(location), 201

@locations_bp.route('/', methods=['GET'])
def get_locations():
    locations = Location.query.all()
    return locations_schema.jsonify(locations), 200

@locations_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_location(id):
    location = Location.query.get_or_404(id)
    data = request.get_json()
    errors = location_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items():
        setattr(location, key, value)
    db.session.commit()
    return location_schema.jsonify(location), 200

@locations_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_location(id):
    location = Location.query.get_or_404(id)
    db.session.delete(location)
    db.session.commit()
    return '', 204
