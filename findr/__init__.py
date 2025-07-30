from flask import Blueprint
from .routes import *

# Create a Blueprint for Findr
findr_bp = Blueprint('findr', __name__, template_folder='templates')

# Register Findr routes
register_findr_routes(findr_bp)