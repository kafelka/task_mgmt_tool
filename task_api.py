import sqlite3
from db_connection import add_task, delete_task, update_task, get_all_tasks
from flask import Flask, request, jsonify, g
app = Flask(__name__)

def get_db(): #from Flask documentation
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("task_management.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()


@app.route("/addTask", methods=["POST"])
def api_add_task():
    content = request.json
    conn = get_db()
    name = content.get("name", None)
    description = content.get("description", None)
    status = content.get("status", None)
    important = content.get("important", None)
    date = content.get("date", None) #to do: validate date format yyyy-mm-dd
    if None not in [name, description, status, important, date]:
        add_task(conn, name, description, status, important, date)
        return 201 #http status: created
    else:
        return 400 #bad request


@app.route("/deleteTask/<int:taskId>", methods=["DELETE"])
def api_delete_task(taskId):
    conn = get_db()
    delete_task(conn, id)
    return 200 #success



@app.route('/updateTask/<int:taskId>', methods=["PUT"])
def api_update_task(taskId):
    content = request.json
    conn = get_db()
    name = content.get("name", None)
    description = content.get("description", None)
    status = content.get("status", None)
    important = content.get("important", None)
    date = content.get("date", None) #to do: validate date format yyyy-mm-dd
    update_task(conn, name, description, status, important, date)


@app.route("/allTasks", methods=["GET"])
def api_get_all_tasks():
    conn = get_db()
    result = get_all_tasks(conn)
    return jsonify(result)




if __name__ == '__main__':
    app.run(debug=True) 
