from flask import request, jsonify, Blueprint
from flask_jwt_extended import jwt_required
from models.employee import Employee
from app import db
from schema import employee_schema, employees_schema

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['POST'])
@jwt_required()
def add_employee():
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    employee = Employee(**data) # Creating a new Employee record #
    db.session.add(employee)
    db.session.commit()  # Commit the new employee to the database #
    return employee_schema.jsonify(employee), 201 # The new employee is returned in JSON format #

@employees_bp.route('/', methods=['GET'])
def get_employees(): # Query all Employee records from the database #
    employees = Employee.query.all()
    return employees_schema.jsonify(employees), 200 # Return the list of employees in JSON format #

@employees_bp.route('/<int:id>', methods=['PUT'])
@jwt_required()
def update_employee(id): # Retrieve the employee by ID, or return 404 if not found #
    employee = Employee.query.get_or_404(id)
    data = request.get_json()
    errors = employee_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    for key, value in data.items(): # Update the employee's attributes #
        setattr(employee, key, value)
    db.session.commit() # Commit the changes to the database #
    return employee_schema.jsonify(employee), 200 # Return the updated employee in JSON format #

@employees_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_employee(id):  # Retrieve the employee by ID, or return 404 if not found #
    employee = Employee.query.get_or_404(id)
    db.session.delete(employee) # Mark the employee record for deletion #
    db.session.commit() # Commit the deletion to the database #
    return '', 204
