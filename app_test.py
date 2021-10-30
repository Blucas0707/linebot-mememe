import unittest
import json
from common.init.init import create_app, db, Task
from module.task.task import init_task

class TestRoute(unittest.TestCase):
    def setUp(self):
        self.app = create_app("testing")
        init_task(self.app)
        self.client = self.app.test_client()
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()
        # create mock data
        createTaskData = Task("test", 0)
        with self.app.app_context():
            db.session.add(createTaskData)
            db.session.commit()
    
    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
    
    # check index page "/"
    def test_index(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)
    
    # check GET /tasks (list tasks)
    def test_getTaskList_200(self):
        res = self.client.get("/tasks")
        self.assertEqual(res.status_code, 200)

    # check POST /task  (create task)
    def test_createTask_201(self):
        req = {
                "name": "買晚餐"
                }
        res = self.client.post("/task", 
                                data=json.dumps(req), 
                                content_type='application/json',
                            )
        self.assertEqual(res.status_code, 201)
    
    # POST Fail - name = ""
    def test_createTask_Not_201(self):
        req = {
                "name": ""
                }
        res = self.client.post("/task", 
                                data=json.dumps(req), 
                                content_type='application/json',
                            )
        self.assertNotEqual(res.status_code, 201)
    
    # check PUT /task/<id> (update task)
    def test_updateTask_200(self):
        req = {
                "name": "test",
                "status": 1,
                "id": 1,
                }
        res = self.client.put("/task/1", 
                                data=json.dumps(req), 
                                content_type='application/json',
                            )
        self.assertEqual(res.status_code, 200)
    
    # POST Fail - name = "noexist"
    def test_updateTask_NOT_200(self):
        req = {
                "name": "noexist",
                "status": 1,
                "id": 1,
                }
        res = self.client.put("/task/1", 
                                data=json.dumps(req), 
                                content_type='application/json',
                            )
        self.assertNotEqual(res.status_code, 200)
    
    # check DELETE /task/<id> 
    def test_deleteTask(self):
        res = self.client.delete("/task/1")
        self.assertEqual(res.status_code, 200)
    
    # DELETE Fail - id notexists
    def test_deleteTask_NOT_200(self):
        res = self.client.delete("/task/-1")
        self.assertNotEqual(res.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()