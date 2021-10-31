from flask import request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage
from module.task.resource import findMemeImage, findTrachTalk
import random

from dotenv import load_dotenv
import os
load_dotenv()

LINEBOT_CHANNEL_ACCESS_TOKEN = os.environ.get("LINEBOT_CHANNEL_ACCESS_TOKEN")
LINEBOT_CHANNEL_SECRET = os.environ.get("LINEBOT_CHANNEL_SECRET")
print(LINEBOT_CHANNEL_ACCESS_TOKEN,LINEBOT_CHANNEL_SECRET)
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
    # meme Image
    @handler.add(MessageEvent, message=TextMessage)
    def memeImage(event):
        text = event.message.text
        if text[0] == "M":
            keyword = text[1:]
            
            MemeImageUrl = findMemeImage(keyword)
            print(MemeImageUrl)
            imageMsg = ImageSendMessage(
                original_content_url=MemeImageUrl,
                preview_image_url=MemeImageUrl
            )

            line_bot_api.reply_message(
                event.reply_token,
                imageMsg
            )
        elif text[0] == "T":
            id = random.randint(1,86)
            trashTalkMsg = findTrachTalk(id)
            resText = "幹話語錄#" +str(id)+"-"+ trashTalkMsg
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=resText)
            )