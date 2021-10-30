from module.task.handler.task_handler import handler as task_handler

def init_task(app):
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