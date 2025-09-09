from flask import Flask, jsonify
# from pymongo import MongoClient
import json
# import os
# from dotenv import load_dotenv

# load_dotenv()

app = Flask(__name__)

# client = MongoClient(os.getenv("MONGO_URI"))
# db = client[os.getenv("DB_NAME")]
# collection = db[os.getenv("COLLECTION_NAME")]


@app.route("/api")
def api_data():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)