from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def index():
    return render_template("index.html")

@pages_bp.route("/level/<int:n>")
def level(n):
    # TODO: check if user has unlocked that level
    
    try:
        return render_template(f"levels/{n}.html")
    except TemplateNotFound:
        abort(404)
