from flask import jsonify, Blueprint

home_bp = Blueprint('home', __name__)

@home_bp.route('/', methods=['GET'])
def index():
    resp = jsonify("OK")
    resp.status_code
    return resp