from flask import Blueprint
from CatalogController import get_all

routes_blueprint = Blueprint('routes-blueprint', __name__)

routes_blueprint.route('/catalog', methods=['GET'])(get_all)