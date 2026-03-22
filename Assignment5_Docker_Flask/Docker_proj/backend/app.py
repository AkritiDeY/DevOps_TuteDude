from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

client = MongoClient(os.environ.get("MONGO_URI"))
db = client["DevOps"]
collection = db["students"]


#Submit method to provide input to the form and submit 
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        name   = data.get("name")
        email  = data.get("email")
        course = data.get("course")

        # taking each input, if not there then throw error..
        if not name or not email or not course:
            return jsonify({"success": False, "error": "All fields are required."}), 400

        # inserting the data into the Db..
        collection.insert_one({"name": name, "email": email, "course": course})

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
