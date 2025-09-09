from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]

# --- Form Page ---
@app.route("/")
def index():
    return render_template("form.html")

# --- Form Submission ---
@app.route("/submit", methods=["POST"])
def submit():
    try:
        name = request.form.get("name")
        email = request.form.get("email")

        if not name or not email:
            return render_template("form.html", error="All fields are required!")

        collection.insert_one({"name": name, "email": email})
        return redirect(url_for("success"))

    except Exception as e:
        return render_template("form.html", error=f"Error: {str(e)}")

# --- Success Page ---
@app.route("/success")
def success():
    return "Data submitted successfully"

if __name__ == "__main__":
    app.run(debug=True)