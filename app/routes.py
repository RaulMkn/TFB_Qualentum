from flask import Blueprint, request, jsonify
from app.models import Data
from app import db

data_routes = Blueprint("data_routes", __name__)


@data_routes.route("/data", methods=["POST"])
def insert_data():
    try:
        data = request.json
        if not data or "name" not in data:
            return {"message": "'name' is required"}, 400

        name = data.get("name").strip()
        if not name:
            return {"message": "'name' cannot be empty."}, 400

        current_data = Data.query.filter_by(name=name).first()
        if current_data:
            return {"message": "Data already exists."}, 409

        new_data = Data(name=name)
        db.session.add(new_data)
        db.session.commit()
        return jsonify({"message": "Data inserted successfully",
                        "id": new_data.id}), 201
    except Exception as e:
        db.session.rollback()
        return {"message": f"An error occurred: {str(e)}"}, 500


@data_routes.route("/data", methods=["GET"])
def get_all_data():
    try:
        data_list = [{"id": data.id,
                      "name": data.name} for data in Data.query.all()]
        return jsonify(data_list), 200
    except Exception as e:
        return {"message": f"An error occurred: {str(e)}"}, 500


@data_routes.route("/data/<int:id>", methods=["DELETE"])
def delete_data(id):
    try:
        element_to_delete = db.session.get(Data, id)
        if not element_to_delete:
            return {"message": "Data not found."}, 404

        db.session.delete(element_to_delete)
        db.session.commit()
        return {"message": "Data deleted successfully."}, 200
    except Exception as e:
        db.session.rollback()
        return {"message": f"An error occurred: {str(e)}"}, 500
