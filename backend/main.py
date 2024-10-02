from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId
from config import uri
from parser import parse_user
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_db(uri):
    client = MongoClient(uri)
    return client['udata']

@app.route('/api/users', methods=['GET'])
def get_users():
    try:
        db = get_db(uri)
        users = list(db['udata_collection'].find())
        users_dict = [{**user, "_id": str(user["_id"])} for user in users]
        return jsonify(users_dict)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    try:
        db = get_db(uri)
        user = db['udata_collection'].find_one({"username": username})
        if user is None:
            return jsonify({"error": "Not found"}), 404
        user['_id'] = str(user['_id'])  
        return jsonify(user)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/users', methods=['POST'])
def create_user():
    user_data = request.json
    user = parse_user(user_data)  
    db = get_db(uri)
    result = db['udata_collection'].insert_one(user)
    return jsonify({"id": str(result.inserted_id)}), 201

@app.route('/api/users/<username>', methods=['PUT'])
def update_user(username):
    user_data = request.json
    db = get_db(uri)
    db['udata_collection'].update_one({"username": username}, {"$set": user_data})
    return jsonify({"message": "User updated"})

@app.route('/api/users/<username>', methods=['DELETE'])
def delete_user(username):
    db = get_db(uri)
    db['udata_collection'].delete_one({"username": username})
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)
