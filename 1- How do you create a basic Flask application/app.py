from flask import Flask, render_template

# Create Flask app instance
app = Flask(__name__)

# Define route for homepage
@app.route("/")
def home():
    return render_template("index.html")

# Run app
if __name__ == "__main__":
    app.run(debug=True)
