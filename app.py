#coding=UTF-8 
from module.task.task import init_task
from common.init.init import create_app
import os
app = create_app("development")

init_task(app)

if __name__=="__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug = True)