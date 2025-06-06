from flask import jsonify, Blueprint

home = Blueprint('home', __name__)

@home.route('/', methods=['GET'])
def index():
    resp = jsonify("OK")
    resp.status_code
    return resp