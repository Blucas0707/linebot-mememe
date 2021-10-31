#coding=UTF-8 
from module.task.task import init_task
from common.init.init import create_app
app = create_app("development")

init_task(app)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug = True)