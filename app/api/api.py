from flask import Blueprint, jsonify, request, session, abort

api_bp = Blueprint("api", __name__)


@api_bp.route("/submit/<int:n>", methods=["POST"])
def submit(n):
    completed_levels = session.get("completed_levels", None)
    if completed_levels is None:
        completed_levels = [0]  # level 0 is always completed

    if n-1 not in completed_levels:
        abort(403, description="Level is not unlocked.")

    data = request.get_json()
    code = data.get("code")

    if n == 1:
        if code == "tojezelolahko":
            completed_levels.append(n)
            session["completed_levels"] = completed_levels
            return jsonify({"result": "correct"})
        
    # else if ...
    
    return jsonify({"result": "incorrect"})


@api_bp.route("/clue/<int:n>", methods=["GET"])
def clue(n):
    if n-1 not in session.get("completed_levels", [0]):
        abort(403, description="Level is not unlocked.")

    # example:
    if (n == 1):
        return jsonify({
            "clue": "Inspect image."
        })
    # ...
    
