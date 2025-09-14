from flask import Flask, request, render_template

# ---- Create the Flask app ----
app = Flask(__name__)

# ---- Route ----
@app.route('/', methods=['GET', 'POST'])
@app.route('/register', methods=['GET', 'POST'])
def register():
    errors = []
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')

        if not username or username.strip() == "":
            errors.append("Username is required.")
        if not age:
            errors.append("Age is required.")
        elif not age.isdigit():
            errors.append("Age must be a number.")
        elif int(age) < 18:
            errors.append("You must be at least 18 years old.")

        if not errors:
            return f"Welcome {username}, you are registered!"

    return render_template('register.html', errors=errors)

# ---- Run the app ----
if __name__ == "__main__":
    app.run(debug=True)
