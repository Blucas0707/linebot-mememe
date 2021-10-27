from module.task.controller.task_controller import controller as task_controller
import sys
sys.path.append("....")
from base.response.type import StatusCode
from base.response.response import response

class Handler:
    def __init__(self):
        print("initHandler")

    # @Accept application/json
    # @Success 200 response{data}
    # @Router /tasks [get]
    def getTaskList(self):
        resp, err = task_controller.getTaskList()
        if err is not None:
            return response.writeErrorResponse(resp, err)
        statuscode = StatusCode["Success"]
        return response.writeDataResponse(resp, statuscode)

    # @Accept application/json
    # @Success 201 response{data}
    # @Router /task [post]
    def createTask(self):
        resp, err = task_controller.createTask()
        if err is not None:
            return response.writeErrorResponse(resp, err)
        statuscode = StatusCode["CreateSuccess"]
        return response.writeDataResponse(resp, statuscode)

    # @Accept application/json
    # @Success 200 response{data}
    # @Router /task/<id> [put]
    def updateTaskId(self,id):
        resp, err = task_controller.updateTaskId(id)
        if err is not None:
            return response.writeErrorResponse(resp, err)
        statuscode = StatusCode["Success"]
        return response.writeDataResponse(resp, statuscode)

    # @Accept application/json
    # @Success 200 response{data}
    # @Router /task/<id> [delete]
    def deleteTaskId(self,id):
        resp, err = task_controller.deleteTaskId(id)
        if err is not None:
            return response.writeErrorResponse(resp, err)
        statuscode = StatusCode["Success"]
        return response.writeSuccessResponse(resp, statuscode)

handler = Handler()