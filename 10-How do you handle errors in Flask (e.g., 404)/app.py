from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the homepage!"

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    # You can return a custom template or a message
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
