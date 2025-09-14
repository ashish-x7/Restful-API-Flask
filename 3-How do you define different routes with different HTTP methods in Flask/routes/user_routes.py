from flask import Blueprint, request, render_template
from services.user_service import get_user_by_name

user_bp = Blueprint("user", __name__)

@user_bp.route("/", methods=["GET"])
def user_home():
    return "Welcome to User Home!"

@user_bp.route("/profile", methods=["POST"])
def user_profile():
    name = request.form.get("name")
    user = get_user_by_name(name)
    return f"Hello {user}"
