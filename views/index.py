from flask import render_template
from .app import app

@app.route("/")
def index():
    tasks = []
    return render_template("index.html", tasks=tasks)
