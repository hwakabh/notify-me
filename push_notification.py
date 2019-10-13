import urllib.request
import urllib.parse
import os
import json

LINE_CHANNEL_ACCESS_TOKEN = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
LINE_USER_ID = os.getenv('LINE_USER_ID', None)

URL = 'https://api.line.me/v2/bot/message/push'
HEADERS = {
    'User-Agent': 'Mozilla',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer {}'.format(LINE_CHANNEL_ACCESS_TOKEN)
}

RAW_DATA = {
    'to': LINE_USER_ID,
    'messages': [
        {
            'type': 'text',
            'text': 'Hello.'
        },
        {
            'type': 'text',
            'text': 'Push notification from Python.'
        }
    ]
}

DATA = json.dumps(RAW_DATA).encode('utf-8')
req = urllib.request.Request(
    url=URL,
    headers=HEADERS,
    data=DATA
)

with urllib.request.urlopen(req) as res:
    body = res.read()

print(json.loads(body.decode('utf-8')))
