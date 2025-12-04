from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__)

# Here add:
# - endpoint that returns clues
# - endpoint that checks if submited code is right
#   if it is, add that level to session so we can track what levels has user complete
#   for example add it to list: [1, 2] means that user completes levels 1 and 2


@api_bp.route("/submit/<int:n>")
def submit(n):
    # check if user has unlocked n level 
    # data will be given with post request
    return;

@api_bp.route("/clue/<int:n>")
def clue(n):
    # check if user has unlocked n level 

    # example:
    if (n == 1):
        return jsonify({
            "clue": "Inspect image."
        })
    # ...
    
