from flask import Blueprint, jsonify, request
from flask_cors import cross_origin


app_route = Blueprint('hangman', __name__, url_prefix="/v0.1/hangman")


@app_route.route("/checkletter", methods=["POST"])
@cross_origin()
def check_letter():
    json_data = request.get_json()
    return jsonify(json_data)
