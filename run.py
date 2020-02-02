from linebot import LineBotApi
from linebot.models import TextSendMessage

import os
import sys
import time
from datetime import datetime
from datetime import timedelta
from datetime import timezone


# Retrieve contents to push if it's time
def get_message_context(current_time, conf):
    for c in conf:
        if c['time'] == current_time:
            return c['text']


# main functions with closed-loops
if __name__ == "__main__":
    print('>>> Booting up the script ...')
    print('>>> Init: Getting configs for pushing messages')
    USER_ID = os.environ.get('LINE_USER_ID')
    ACCESS_TOKEN = os.environ.get('LINE_ACCESS_TOKEN')
    TZ = os.environ.get('TZ')

    if (USER_ID is None) or (ACCESS_TOKEN is None):
        print('Failed to fetch USER_ID and ACCESS_TOKEN for push messages, confirm to run the commands:')
        print('\t export LINE_USER_ID=\'USER_ID_TO_PUSH\'')
        print('\t export LINE_ACCESS_TOKEN=\'BOT_ACCESS_TOKEN\'')
        sys.exit(1)

    print('>>> Init: Loading contents in messages.py')
    import messages
    candidate_times = [c['time'] for c in messages.msg]

    print('>>> Init: Create LINE API Instances')
    endpoint = LineBotApi(channel_access_token=ACCESS_TOKEN)

    print('>>> Starting closed-loops for checking time ...')
    while True:
        t = datetime.now().strftime('%H-%M')
        # Modify timezone if not configured
        if os.getenv('TZ') != 'Asia/Tokyo':
            tz = timezone(timedelta(hours=9), 'JST')
            t = datetime.now(tz).strftime('%H-%M')

        if (t in candidate_times):
            MESSAGE = get_message_context(
                current_time=t,
                conf=messages.msg
                )
            print('Calling LINE API with SDK method push_message() ...')
            endpoint.push_message(
                USER_ID,
                TextSendMessage(
                    text=MESSAGE
                )
            )
        else:
            print('Current time: {} : nothing to do for messaging.'.format(datetime.now()))
            pass

        # Reconcilation Loop interval is 1 min by default
        time.sleep(60)