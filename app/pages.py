from flask import Blueprint, render_template, abort, session
from jinja2 import TemplateNotFound
from .functions import get_number_of_levels

pages_bp = Blueprint("pages", __name__)

@pages_bp.route("/")
def index():
    return render_template("index.html")

@pages_bp.route("/finish")
def finish():
    total_levels = get_number_of_levels()
    if session.get("completed_levels", [0])[-1] != total_levels:
        abort(403, description="You have not completed all levels yet.")
        
    return render_template("finish.html")

@pages_bp.route("/levels/<int:n>")
def levels(n):
    if n-1 not in session.get("completed_levels", [0]):
        abort(403, description="Level is not unlocked.")
    
    try:
        return render_template(f"levels/{n}.html")
    except TemplateNotFound:
        abort(404)
