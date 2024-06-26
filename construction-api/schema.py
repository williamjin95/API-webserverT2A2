from flask_marshmallow import Marshmallow
from models.user import User
from models.employee import Employee
from models.location import Location
from models.hour import Hour

ma = Marshmallow()

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User

class EmployeeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Employee

class LocationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Location

class HourSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hour

user_schema = UserSchema()
users_schema = UserSchema(many=True)
employee_schema = EmployeeSchema()
employees_schema = EmployeeSchema(many=True)
location_schema = LocationSchema()
locations_schema = LocationSchema(many=True)
hour_schema = HourSchema()
hours_schema = HourSchema(many=True)
