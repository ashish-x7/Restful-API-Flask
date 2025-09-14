from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Sessions ke liye secret key

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username  # Store session
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/profile')
def profile():
    if 'username' in session:
        return render_template('profile.html', username=session['username'])
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove session
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
