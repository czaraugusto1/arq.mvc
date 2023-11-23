from flask import render_template
from .app import app

@app.route("/remove")
def remove():
    tasks = []
    task_id = request.args.get("id")
    if task_id is not None:
        tasks.remove(tasks[int(task_id)])
    return render_template("index.html", tasks=tasks)
