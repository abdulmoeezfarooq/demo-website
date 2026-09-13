"""
Quetta Mehfil Chai Khana — website served with Python (Flask).

This is the same site as the HTML file, now served by a small Python
web app instead of being a static file. Useful if you want to add
dynamic behaviour later (a real menu database, an order form, etc.)
or deploy somewhere that runs Python.

Setup:
    pip install flask
    python app.py

Then open http://localhost:5000 in your browser.

Folder layout expected:
    app.py
    templates/
        index.html   <- the site's markup (already included)
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
