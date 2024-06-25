from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Initialize SQLAlchemy and Marshmallow
db = SQLAlchemy()
ma = Marshmallow()

# Create the API blueprint
api_bp = Blueprint('api', __name__)

# Import models to ensure they are registered with SQLAlchemy
from models.user import User
from models.employee import Employee
from models.location import Location
from models.hour import Hour

# Import and register blueprints
from .auth import api_bp as auth_bp
from .employees import api_bp as employees_bp
from .hours import api_bp as hours_bp
from .locations import api_bp as locations_bp

api_bp.register_blueprint(auth_bp, url_prefix='/auth')
api_bp.register_blueprint(employees_bp, url_prefix='/employees')
api_bp.register_blueprint(hours_bp, url_prefix='/hours')
api_bp.register_blueprint(locations_bp, url_prefix='/locations')
