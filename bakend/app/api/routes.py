from flask import Blueprint
from .controllers import create_block, get_chain, validate_chain, hash_data

api_bp = Blueprint("api", __name__)

api_bp.route("/block", methods=["POST"])(create_block)
api_bp.route("/chain", methods=["GET"])(get_chain)
api_bp.route("/validate", methods=["GET"])(validate_chain)
api_bp.route("/hash", methods=["POST"])(hash_data)