import urllib.request
import urllib.parse
import os
import json
import datetime
import time

import messages

# Configurations for pushing to LINE Messaging API
LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
LINE_USER_ID = os.getenv('LINE_USER_ID', None)

URL = 'https://api.line.me/v2/bot/message/push'
HEADERS = {
    'User-Agent': 'Mozilla',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(LINE_CHANNEL_ACCESS_TOKEN)
}
RECONCILATION_PERIOD_SEC = 60


def pushing_messages(text_message):
    DATA = json.dumps(text_message).encode('utf-8')
    req = urllib.request.Request(
        url=URL,
        headers=HEADERS,
        data=DATA
    )

    with urllib.request.urlopen(req) as res:
        body = res.read()
    if res.getcode() == 200:
        print('POST success, you might get push notifications soon.')
    else:
        print('Return-Code: {} | Failed to POST ...'.format(res.getcode()))

    print('Response body : \n{}'.format(json.loads(body.decode('utf-8'))))


def get_message_body(t):
    msg = ''
    candidate_times = [m.get('time') for m in messages.msg]
    print(candidate_times)

    if t.strftime('%H-%M') in candidate_times:
        index = candidate_times.index(t.strftime('%H-%M'))
        print(index)
        msg = messages.msg[index]['text']

    return msg


while True:
    print('Starting closed loop, checking time...')
    time.sleep(RECONCILATION_PERIOD_SEC)
    now = datetime.datetime.now()

    push_text = get_message_body(t=now)
    if push_text == '':
        print('>>> Current Time : {} | It is not time to remind. nothing to do.'.format(now))
        continue
    else:
        print('>>> Current Time : {} | Time to remind. Run push-notification.'.format(now))
        push_data = {
            'to': LINE_USER_ID,
            'messages': [
                {
                    'type': 'text',
                    'text': push_text
                }
            ]
        }
        pushing_messages(push_data)

