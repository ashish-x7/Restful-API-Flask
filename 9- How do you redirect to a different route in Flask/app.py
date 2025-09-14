from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    # After login, redirect to home page
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
