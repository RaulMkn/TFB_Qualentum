import pytest
from unittest.mock import patch

def test_insert_data_success(client):
    response = client.post("/data", json={"name": "Alice"})
    assert response.status_code == 201
    assert b"Data inserted successfully" in response.data

def test_insert_duplicate_data(client):
    client.post("/data", json={"name": "Bob"})
    response = client.post("/data", json={"name": "Bob"})
    assert response.status_code == 409
    assert b"Data already exists" in response.data

def test_insert_data_missing_name(client):
    response = client.post("/data", json={})
    assert response.status_code == 400
    assert response.get_json()["message"] == "Invalid input. 'name' is required."

def test_insert_data_empty_name(client):
    response = client.post("/data", json={"name": "   "})
    assert response.status_code == 400
    assert response.get_json()["message"] == "Invalid input. 'name' cannot be empty."


def test_insert_data_db_error(client):
    with patch("app.routes.db.session.commit", side_effect=Exception("DB error")):
        response = client.post("/data", json={"name": "DBFail"})
        assert response.status_code == 500
        assert b"An error occurred" in response.data

def test_get_all_data(client):
    client.post("/data", json={"name": "Charlie"})
    response = client.get("/data")
    assert response.status_code == 200
    json_data = response.get_json()
    assert any(item["name"] == "Charlie" for item in json_data)

def test_get_all_data_db_error(client):
    with patch("app.routes.Data.query") as mock_query:
        mock_query.all.side_effect = Exception("DB error")
        response = client.get("/data")
        assert response.status_code == 500
        assert b"An error occurred" in response.data

def test_delete_existing_data(client):
    client.post("/data", json={"name": "DeleteMe"})
    get_response = client.get("/data")
    item_id = get_response.get_json()[0]["id"]

    delete_response = client.delete(f"/data/{item_id}")
    assert delete_response.status_code == 200
    assert b"Data deleted successfully" in delete_response.data

def test_delete_non_existing_data(client):
    response = client.delete("/data/9999")
    assert response.status_code == 404
    assert b"Data not found" in response.data

def test_delete_data_db_error(client):
    client.post("/data", json={"name": "ToFailDelete"})
    get_response = client.get("/data")
    item_id = get_response.get_json()[0]["id"]

    with patch("app.routes.db.session.commit", side_effect=Exception("DB error")):
        response = client.delete(f"/data/{item_id}")
        assert response.status_code == 500
        assert b"An error occurred" in response.data
