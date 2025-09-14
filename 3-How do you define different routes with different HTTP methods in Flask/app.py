from flask import Flask
from routes.home_routes import home_bp
from routes.user_routes import user_bp

app = Flask(__name__)

# Register Blueprints (modular routes)
app.register_blueprint(home_bp)
app.register_blueprint(user_bp, url_prefix="/user")

if __name__ == "__main__":
    app.run(debug=True)
