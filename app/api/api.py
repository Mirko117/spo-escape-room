from flask import Blueprint, jsonify, request, session, abort, redirect

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
        
    if n == 2:
        if code == "zeloZahtevnoGeslo":
            completed_levels.append(n)
            session["completed_levels"] = completed_levels
            return jsonify({"result": "correct"})
    
    if n == 3: 
        if code == "184161785232162357326496453395931":
            completed_levels.append(n)
            session["completed_levels"] = completed_levels
            return jsonify({"result": "correct"})
        
    if n == 4:
        if code == "KONEC":
            completed_levels.append(n)
            session["completed_levels"] = completed_levels
            return jsonify({"result": "correct", "status": 302, "url": "/finish"})
    
    return jsonify({"result": "incorrect"})


@api_bp.route("/clue/<int:n>", methods=["GET"])
def clue(n):
    if n-1 not in session.get("completed_levels", [0]):
        abort(403, description="Level is not unlocked.")

    if (n == 1):
        return jsonify({
            "clue": "Inspect element."
        })
    if (n == 2):
        return jsonify({
            "clue": "URL (base64)"
        })
    
    if (n == 3):
        return jsonify({
            "clue": "Napiši kodo s pomočjo slike."
        })
    
    if (n == 4):
        return jsonify({
            "clue": "Klikni na gumb 'Klikni me' (čeprav je onemogočen)."
        })
