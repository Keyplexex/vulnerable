from flask import Flask, request
import sqlite3

app = Flask(__name__)
app.config['DEBUG'] = True

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def index():
    return "Vulnerable demo app"

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("password")

    conn = get_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)

    user = cursor.fetchone()
    return "Login success" if user else "Login failed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
