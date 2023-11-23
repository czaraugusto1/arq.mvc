from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Definindo tasks fora das funções para manter o estado entre as requisições
tasks = []

@app.route("/")
def index():
    tasks_dict = {index: task for index, task in enumerate(tasks)}
    return render_template("index.html", tasks=tasks_dict)

@app.route("/remove_task")
def remove_task():
    task_id = request.args.get("id")
    if task_id is not None:
        try:
            tasks.pop(int(task_id))  # Remove o item da lista pelo índice
        except IndexError:
            pass  # Ignora se o índice não for válido
    return redirect(url_for('index'))

@app.route("/add_task", methods=["POST"])
def add_task():
    new_task = request.form.get("task_name")
    if new_task:
        tasks.append(new_task)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/remove_task")
def remove_task():
    task_id = request.args.get("id")
    if task_id is not None:
        try:
            tasks.pop(int(task_id))  # Remove o item da lista pelo índice
        except (IndexError, ValueError):
            pass  # Ignora se o índice não for válido
    return redirect(url_for('index'))
