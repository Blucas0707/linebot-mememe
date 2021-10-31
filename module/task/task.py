from module.task.handler.task_handler import handler as task_handler
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from dotenv import dotenv_values

#load .env config
# config = dotenv_values(".env")
LINEBOT_CHANNEL_ACCESS_TOKEN="BTZp8SjZNwsLvN3ryN6qA9+iw0FTNqrt0wceAGxw4e/D+NGX5kSxvjrOCY7lOCuoRYWfo90N39zYXAA7gsDYvebYI+CiADIRpEbjUL0sS6Kj7NmQIU3Reb62hIu2/+dhee+u2MGfev+LBKznetu8vgdB04t89/1O/w1cDnyilFU="
LINEBOT_CHANNEL_SECRET="a97c765c954b3b2d8c86aa3ebf3b479a"
line_bot_api = LineBotApi(LINEBOT_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINEBOT_CHANNEL_SECRET)

def init_task(app):

    # get Line 
    @app.route("/callback", methods=["POST"])
    def callback():
        signature = request.headers['X-Line-Signature']

        body = request.get_data(as_text=True)
        app.logger.info("Request body: " + body)
        
        try:
            print(body, signature)
            handler.handle(body, signature)
            
        except InvalidSignatureError:
            abort(400)

        return 'OK'
    # 學你說話
    @handler.add(MessageEvent, message=TextMessage)
    def pretty_echo(event):
        
        if event.source.user_id != "Udeadbeefdeadbeefdeadbeefdeadbeef":
            
            # Phoebe 愛唱歌
            pretty_note = '♫♪♬'
            pretty_text = ''
            
            for i in event.message.text:
            
                pretty_text += i
                pretty_text += random.choice(pretty_note)
        
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=pretty_text)
            )
    
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