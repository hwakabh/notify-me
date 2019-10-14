import os

from flask import Flask
from flask import request

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import TextMessage
from linebot.models import MessageEvent


# Set credentilas securely
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)

app = Flask(__name__)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route('/callback', methods=['POST'])
def callback():
    print('>>> Calllbacked.')
    sig = request.headers['X-Line-Signature']
    req = request.get_data(as_text=True)
    print('>>> sig : \n{}'.format(sig))
    print('>>> req : \n{}'.format(req))
    try:
        handler.handle(req, sig)
    except:
        pass
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'debug':
        line_bot_api.reply_message(event.reply_token, TextSendMessage('Okay, here are each IDs.'))

        if hasattr(event.source,'group_id'):
            os.environ['LINE_GROUP_ID'] = event.source.group_id
            line_bot_api.reply_message(event.reply_token, TextSendMessage(event.source.group_id)

        if hasattr(event.source,'room_id'):
            os.environ['LINE_ROOM_ID'] = event.source.room_id
            line_bot_api.reply_message(event.reply_token, TextSendMessage(event.source.room_id)

        return

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hope this help, thanks.'))
        # TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    print('>>> Starting Flask apps as background process...')
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
