from flask import Flask, render_template, request, jsonify
from routes import get_route
import os

app = Flask(__name__)

# Locations List
locations = [
    "A101",
    "A102",
    "Corridor1",
    "Lab1",
    "Library"
]

# Home Page
@app.route("/")
def home():
    return render_template("index.html")


# Route Finder (Website)
@app.route("/find_route", methods=["POST"])
def find_route():

    start = request.form["start"]
    destination = request.form["destination"]

    result = get_route(
        start,
        destination
    )

    return render_template(
        "result.html",
        path=result["path"],
        distance=result["distance"]
    )


# GET - View All Locations
@app.route("/locations", methods=["GET"])
def get_locations():

    return jsonify({
        "locations": locations
    })


# POST - Add Location
@app.route("/location", methods=["POST"])
def add_location():

    data = request.get_json()

    if not data or "name" not in data:
        return jsonify({
            "error": "Location name required"
        }), 400

    name = data["name"]

    locations.append(name)

    return jsonify({
        "message": "Location Added",
        "location": name
    })


# PUT - Update Location
@app.route("/location/<old_name>", methods=["PUT"])
def update_location(old_name):

    data = request.get_json()

    if not data or "new_name" not in data:
        return jsonify({
            "error": "New location name required"
        }), 400

    if old_name not in locations:
        return jsonify({
            "error": "Location Not Found"
        }), 404

    index = locations.index(old_name)

    locations[index] = data["new_name"]

    return jsonify({
        "message": "Location Updated",
        "new_name": data["new_name"]
    })


# DELETE - Delete Location
@app.route("/location/<name>", methods=["DELETE"])
def delete_location(name):

    if name not in locations:
        return jsonify({
            "error": "Location Not Found"
        }), 404

    locations.remove(name)

    return jsonify({
        "message": "Location Deleted"
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)