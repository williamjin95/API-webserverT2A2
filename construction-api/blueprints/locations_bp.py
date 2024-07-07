from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from models.location import Location
from app import db
from schema import location_schema, locations_schema

locations_bp = Blueprint('locations', __name__)

@locations_bp.route('/', methods=['POST'])
@jwt_required()
def add_location():
    data = request.get_json()
    errors = location_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    location = Location(**data) # Creating a new Location record #
    db.session.add(location)
    db.session.commit() # Commit the new location to the database #
    return location_schema.jsonify(location), 201 # The new location is returned in JSON format #

@locations_bp.route('/', methods=['GET'])
def get_locations(): # Query all Location records from the database #
    locations = Location.query.all()
    return locations_schema.jsonify(locations), 200 # Return the list of locations in JSON format #

@locations_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_location(id): # Retrieve the location by ID, or return 404 if not found #
    location = Location.query.get_or_404(id)
    data = request.get_json()
    errors = location_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items():  # Update the location's attributes #
        setattr(location, key, value)
    db.session.commit() # Commit the changes to the database #
    return location_schema.jsonify(location), 200  # Return the updated location in JSON format #

@locations_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_location(id):  # Retrieve the location by ID, or return 404 if not found
    location = Location.query.get_or_404(id)
    db.session.delete(location) # Mark the location record for deletion #
    db.session.commit() # Commit the deletion to the database #
    return '', 204
