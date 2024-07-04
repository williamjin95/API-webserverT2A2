from flask import request, jsonify, Blueprint
from models.employee import Employee
from app import db
from schema import employee_schema, employees_schema
from flask_jwt_extended import jwt_required

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    employee = Employee(**data)
    db.session.add(employee)
    db.session.commit()
    return employee_schema.jsonify(employee), 201

@employees_bp.route('/', methods=['GET'])
def get_employees():
    employees = Employee.query.all()
    return employees_schema.jsonify(employees), 200

@employees_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_employee(id):
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items():
        setattr(employee, key, value)
    db.session.commit()
    return employee_schema.jsonify(employee), 200

@employees_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employee(id):
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee)
    db.session.commit()
    return '', 204
