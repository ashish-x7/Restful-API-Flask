from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

# URL parameter (path variable)
@app.route('/user/<username>')
def user_profile(username):
    return render_template('user.html', name=username)

# URL + Query parameter example
@app.route('/search')
def search():
    query = request.args.get('q')  # /search?q=flask
    return f"You searched for: {query}"

if __name__ == "__main__":
    app.run(debug=True)
