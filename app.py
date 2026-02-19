from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

# PostgreSQL connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="newpass123",
    port="5432"
)

cursor = conn.cursor()

@app.route("/")
def home():
    return "S4learnHub Python Backend Running 🚀"

# REGISTER
@app.route("/register", methods=["POST"])
def register():
    data = request.json
    username = data["username"]
    email = data["email"]
    password = data["password"]

    try:
        cursor.execute(
            "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
            (username, email, password)
        )
        conn.commit()
        return jsonify({"success": True, "message": "Registration Successful ✅"})
    except:
        conn.rollback()
        return jsonify({"success": False, "message": "Email already exists ❌"})

# LOGIN
@app.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    cursor.execute(
        "SELECT * FROM users WHERE email=%s AND password=%s",
        (email, password)
    )

    user = cursor.fetchone()

    if user:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

if __name__ == "__main__":
    app.run(port=3000, debug=True)
