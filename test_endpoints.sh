#!/bin/bash
# filepath: test_endpoints.sh

BASE_URL="http://127.0.0.1:5000/data"

# Test POST /data (Insert Data)
echo "Testing POST /data (Insert Data)..."
curl -X POST -H "Content-Type: application/json" -d '{"name": "Test Data"}' $BASE_URL
echo -e "\n"

# Test GET /data (Get All Data)
echo "Testing GET /data (Get All Data)..."
curl -X GET $BASE_URL
echo -e "\n"

# Test DELETE /data/<id> (Delete Data)
# Replace <id> with the actual ID of the data you want to delete
echo "Testing DELETE /data/<id> (Delete Data)..."
curl -X DELETE $BASE_URL/1
echo -e "\n"