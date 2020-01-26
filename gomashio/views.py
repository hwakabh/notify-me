import os
from flask import Blueprint
from flask import request

from linebot import LineBotApi
from linebot import WebhookHandler
from linebot.models import TextSendMessage
from linebot.models import TextMessage
from linebot.models import MessageEvent

# Set credentilas for app:gomashio securely
gomashio_channel_access_token = os.getenv('GOMASHIO_CHANNEL_ACCESS_TOKEN', None)
gomashio_channel_secret = os.getenv('GOMASHIO_CHANNEL_SECRET', None)

# Instanciate app:gomashio
gomashio = Blueprint(
    name='gomashio',
    import_name=__name__
)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(gomashio_channel_access_token)
handler = WebhookHandler(gomashio_channel_secret)


@gomashio.route('/callback', methods=['POST'])
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
