from flask import Flask, request
from ..config.db_config import Task as dbTask
import sys
sys.path.append("....")
from common.db.db_sqlite import db
import json


class Model:
    def __init__(self):
        print("initModel")
    def getTaskList(self):
        resp, err = None, None
        try:
            queryTaskList = dbTask.query.order_by(dbTask.id).all()
            print(queryTaskList)
            taskResult = dict()
            taskResult["result"] = []
            for task in queryTaskList:
                temp = dict()
                temp["id"] = task.id
                temp["name"] = task.name
                temp["status"] = task.status
                taskResult["result"].append(temp)
            resp = taskResult
        except:
            err = "ErrServerError"
        finally:
            return resp, err

    def createTask(self):
        taskRequest = request.json
        resp, err = None, None
        # name is empty
        if len(taskRequest["name"]) == 0:
            err = "ErrNullInput"
            return resp, err

        # query first
        queryTask = dbTask.query.filter_by(name=taskRequest["name"]).first()
        if queryTask != None:
            err = "ErrInvalidIndex"
            return resp, err
        try:
            createTaskData = dbTask(taskRequest["name"], 0)
            db.session.add(createTaskData)
            db.session.commit()
            # query result
            queryTask = dbTask.query.filter_by(name=taskRequest["name"]).first()
            taskResult = dict()
            temp = dict()
            temp["id"] = queryTask.id
            temp["name"] = queryTask.name
            temp["status"] = queryTask.status
            taskResult["result"] = temp
            resp = taskResult
        except:
            err = "ErrServerError"
        finally:
            return resp, err

    #Question: I think id is redundant because request is given.
    def updateTaskId(self,id):
        taskRequest = request.json
        print(taskRequest["id"],taskRequest["name"],taskRequest["status"])
        resp, err = None, None

        # name, status or id is empty
        if taskRequest["id"] is None or len(taskRequest["name"]) == 0 or taskRequest["status"] is None :
            err = "ErrNullInput"
            return resp, err
        # status is not 0 or 1
        if taskRequest["status"] != 0 and taskRequest["status"] != 1:
            err = "ErrInvalidIndex"
            return resp, err

        try:
            # query first
            queryTask = dbTask.query.filter_by(name=taskRequest["name"], id=taskRequest["id"]).first()
            if queryTask == None:
                err = "ErrFieldNotFound"
                return "", err
            # update
            queryTask.id = taskRequest["id"]
            queryTask.name = taskRequest["name"]
            queryTask.status = taskRequest["status"]
            db.session.commit()
            queryTask = dbTask.query.filter_by(name=taskRequest["name"], id=taskRequest["id"]).first()
            taskResult = dict()
            temp = dict()
            temp["id"] = queryTask.id
            temp["name"] = queryTask.name
            temp["status"] = queryTask.status
            taskResult["result"] = temp
            resp = taskResult
        except:
            err = "ErrServerError"
        finally:
            return resp, err

    def deleteTaskId(self,id):
        requestId = id
        resp, err = None, None
        # id is empty
        if len(requestId) == 0 or requestId == None:
            err = "ErrNullInput"
            return resp, err
        
        try:
            # query first
            queryTask = dbTask.query.filter_by(id=requestId).first()
            if queryTask == None:
                err = "ErrFieldNotFound"
                return "", err
            db.session.delete(queryTask)
            db.session.commit()
        except:
            err = "ErrServerError"
        finally:
            return resp, err

model = Model()