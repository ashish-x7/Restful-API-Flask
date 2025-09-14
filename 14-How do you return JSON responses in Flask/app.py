from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Server is running"

@app.route("/api/data")
def data():
    return jsonify({"hello": "world", "status": "ok"})

# the if __name__ guard allows python app.py to run directly
if __name__ == "__main__":
    app.run(debug=True)
