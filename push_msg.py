import os

from flask import Flask
from flask import request

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import MessageEvent
 
# Set credentilas securely
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
channel_secret = os.getenv('LINE_CHANNEL_SECRET', None)
line_user_id = os.getenv('LINE_USER_ID', None)

app = Flask(__name__)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route('/callback', methods=['POST'])
def callback():
    sig = request.headers['X-Line-Signature']
    req = request.get_data(as_text=True)
    print('Set request header/body !!')
    print('signature : {}'.format(sig))
    print('request body : {}'.format(req))
    app.logger.info('Request Body : {}'.format(req))
    handler.handle(req, sig)
    return 'OK'


@handler.add(MessageEvent, message=TextSendMessage)
def response_message(event):
        profile = line_bot_api.get_profile(event.source.user_id)
        print(profile)
        print('Got Profile !!')



# def main():
#     messages = TextSendMessage(text="Hello LINE Push notifications.")
#     line_bot_api.push_message(line_user_id, messages=messages)
 
if __name__ == "__main__":
    print('Starting Flask apps...')
    # main()
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    print('Stopping apps.')
