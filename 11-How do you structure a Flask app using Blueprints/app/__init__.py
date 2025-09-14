from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Import and register Blueprints
    from .auth import auth_bp
    from .blog import blog_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(blog_bp, url_prefix='/blog')

    # Add root route
    @app.route('/')
    def home():
        return 'Welcome to the Flask App!'

    return app
