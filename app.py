from flask import Flask, render_template, request
from flask_assets import Bundle, Environment

from todo import todos

app = Flask(__name__)

assets = Environment(app)
js = Bundle("src/*.js", output="dist/main.js")

assets.register("js", js)
js.build()

# Sets base root to index.html


@app.route("/")
def main():
    return render_template('index.html')

# Setup search endpoint


@app.route("/search", methods=["POST"])
def search_todo():
    search_term = request.form.get("search")
    if not len(search_term):
        return render_template("todo.html", todos=[])

    res_todos = []
    for todo in todos:
        if search_term in todo["title"]:
            res_todos.append(todo)
        elif search_term == str(todo["id"]):
            res_todos.append(todo)
        elif search_term == str(todo["completed"]).lower():
            res_todos.append(todo)

    return render_template("todo.html", todos=res_todos)


if __name__ == '__main__':
    app.run(debug=True)
