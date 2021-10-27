from module.task.model.task_model import model as task_model
import json

class Controller:
    def __init__(self):
        print("initController")
    def getTaskList(self):
        return task_model.getTaskList()

    def createTask(self):
        return task_model.createTask()

    def updateTaskId(self,id):
        return task_model.updateTaskId(id)

    def deleteTaskId(self,id):
        return task_model.deleteTaskId(id)

controller = Controller()