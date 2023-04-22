from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix
from linebot import LineBotApi, WebhookHandler
from linebot.models import (MessageEvent,
                            TextMessage,
                            TextSendMessage,
                            StickerMessage,
                            ImageMessage,
                            LocationMessage)
import json
from datetime import datetime , timedelta
from model import asking_people


##Reading Config File####

with open("config.json") as file:
   config_data = json.load(file)

##Setting config value 
mangocluster = config_data["mangocluster"]  ## For connect MongDB
channel_secret = config_data["line_channel_secret"] ## For connect Line
channel_access_token = config_data["line_channel_access_token"] ## For connect Line

####End of Reading config file####


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)



##### Web App code #####



##### End App code #####

####### Line Bot Code #########



line_bot_api = LineBotApi(channel_access_token) 
handler = WebhookHandler(channel_secret)        


@app.route("/line", methods=["GET","POST"])
def home():
    try:
        signature = request.headers["X-Line-Signature"]
        body = request.get_data(as_text=True)
        handler.handle(body, signature)
    except:
        pass
    
    return "Hello Line Chatbot"

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
    print(text)    
    
    if (text=="จำนวนคน"):
        
        qty = asking_people(mangocluster) # Asking people to mongoDB        
        dt = qty[0]['timestamp'] + timedelta(hours=7) # + 7hr for Thai time
        amount = qty[0]['wait_qty']
        date = dt.strftime("%d %b %Y")
        time = dt.strftime("%H:%M %Ssecond")        
        text_out1 = f"Date :{date} "
        text_out2 = f"Time :{time}"
        text_out3 = f"จำนวนคนรอ : {amount} คน"
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=text_out1),
             TextSendMessage(text=text_out2),
             TextSendMessage(text=text_out3)]
            )

@handler.add(MessageEvent, message=StickerMessage)
def handle_sticker_message(event):
    text_out = "ได้รับสติ๊กเกอร์เข้ามา"
    print(event)
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    print(event)
    text_out = "ได้รับรูปภาพเข้ามา"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    
    
    
@handler.add(MessageEvent, message=LocationMessage)
def handle_location_message(event):
    print(event)
    text_out = "ได้รับตำแหน่งที่ตั้งเข้ามา"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=text_out))
    
if __name__ == "__main__":          
    app.run()

