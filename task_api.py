import sqlite3
from db_connection import add_task, delete_task, update_task, get_all_tasks, get_tasks_for_date, get_tasks_between_dates, get_task_by_id
from flask import Flask, request, g, render_template, redirect, abort, url_for
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
   conn = get_db()
   name = request.form.get("task_title", None)
   description = request.form.get("task_description", None)
   status = request.form.get("task_status", None)
   important = request.form.get("task_important", False)
   if important != "True":
       important = "False"
   date = request.form.get("task_date", None)
   if "" not in [name, description, status, important, date]:
       add_task(conn, name, description, status, important, date)
       return redirect(url_for("api_get_all_tasks"))
   else:
       return abort(400) #bad request


@app.route("/deleteTask/<int:taskId>", methods=["POST"]) #DELETE method DOES NOT WORK!!!!!!!!!
def api_delete_task(taskId):
    conn = get_db()
    delete_task(conn, taskId)
    return redirect(url_for("api_get_all_tasks"))  



@app.route('/updateTask/<int:taskId>', methods=["POST"])
def api_update_task(taskId):
    conn = get_db()
    name = request.form.get("task_title", None)
    description = request.form.get("task_description", None)
    status = request.form.get("task_status", None)
    important = request.form.get("task_important", False)
    if important != "True":
        important = "False"
    date = request.form.get("task_date", None) 
    if "" not in [name, description, status, important, date]:
        update_task(conn, taskId, name, description, status, important, date)
        return redirect(url_for("api_get_all_tasks"))
    else:
        return abort(400) #bad request

@app.route("/editTask/<int:taskId>", methods=["GET"])
def api_get_task_by_id(taskId):
    conn = get_db()
    result = get_task_by_id(conn, taskId)
    return render_template("edit.html", task=result[0])


@app.route("/", methods=["GET"])
def api_get_all_tasks():
    conn = get_db()
    result = get_all_tasks(conn)
    return render_template("index.html", tasks=result)



if __name__ == '__main__':
    app.run(debug=True)
