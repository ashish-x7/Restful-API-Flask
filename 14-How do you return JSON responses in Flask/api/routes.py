from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

@api_bp.route("/data")
def get_data():
    return jsonify({
        "name": "Ashish",
        "status": "active",
        "version": 4
    })

@api_bp.route("/error")
def get_error():
    return jsonify({"error": "Something went wrong"}), 400
