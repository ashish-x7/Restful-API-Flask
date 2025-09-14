from flask import render_template
from . import blog_bp

@blog_bp.route('/')
def index():
    return render_template('index.html')

@blog_bp.route('/post/<int:post_id>')
def post(post_id):
    return f"Displaying blog post {post_id}"
