from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    # Redirect to /welcome with query parameters
    return redirect(url_for('welcome', name='Aj', age=25))

# Welcome route
@app.route('/welcome')
def welcome():
    # Get query parameters
    name = request.args.get('name', 'Guest')
    age = request.args.get('age', 'Unknown')
    return render_template('welcome.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
