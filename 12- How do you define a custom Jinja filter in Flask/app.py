from flask import Flask, render_template

app = Flask(__name__)

# --- Custom Jinja Filter ---
@app.template_filter('reverse')
def reverse_string(s):
    return s[::-1]

# --- Route ---
@app.route('/')
def index():
    name = "Flask"
    return render_template('index.html', name=name)

# --- Run App ---
if __name__ == '__main__':
    app.run(debug=True)
