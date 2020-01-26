import os
from flask import Blueprint
from flask import request

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import TextMessage
from linebot.models import MessageEvent

# Set credentilas for app:mediciner securely
mediciner_channel_access_token = os.getenv('MEDICINER_CHANNEL_ACCESS_TOKEN', None)
mediciner_channel_secret = os.getenv('MEDICINER_CHANNEL_SECRET', None)

# Instanciate app:mediciner
mediciner = Blueprint(
    name='mediciner',
    import_name=__name__
)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(mediciner_channel_access_token)
handler = WebhookHandler(mediciner_channel_secret)


@mediciner.route('/callback', methods=['POST'])
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
