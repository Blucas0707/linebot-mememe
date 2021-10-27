#coding=UTF-8 
# task module
from module.task.handler.task_handler import handler as task_handler
# Flask basic config
from flask import Flask, render_template, request
app=Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"]=True

# init db
from common.db.db_sqlite import db
# 設定資料庫位置，並建立 app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db.init_app(app)

# Pages
@app.route("/")
def index():
    msg = ""
    try:
        db.create_all()
        msg = "welcome to gogolook api assignment and db setup successed"
    except:
        msg = "welcome to gogolook api assignment but db setup failed"
    finally:
	    return msg

### 1.  GET /tasks (list tasks)
@app.route("/tasks", methods = ["GET"])
def getTaskList():
	return task_handler.getTaskList()

### 2.  POST /task  (create task)
@app.route("/task", methods = ["POST"])
def createTask():
	return task_handler.createTask()

### 3. PUT /task/<id> (update task)
@app.route("/task/<id>", methods = ["PUT"])
def updateTaskId(id):
	return task_handler.updateTaskId(id)

### 4. DELETE /task/<id> (delete task)
@app.route("/task/<id>", methods = ["DELETE"])
def deleteTaskId(id):
	return task_handler.deleteTaskId(id)

app.run(host="0.0.0.0", port=8080, debug = True)