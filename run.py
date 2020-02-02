from linebot import LineBotApi
from linebot.models import TextSendMessage

import os
import sys

# Check current time for pushing messaging or not
def check_times_to_push():
    pass


# Methods to push messages
def notify_to_user():
    pass


# main functions with closed-loops
if __name__ == "__main__":
    print('>>> Booting up the script ...')
    print('>>> Init: Getting configs for pushing messages')
    USER_ID = os.environ.get('LINE_USER_ID')
    ACCESS_TOKEN = os.environ.get('LINE_ACCESS_TOKEN')

    if (USER_ID is None) or (ACCESS_TOKEN is None):
        print('Failed to fetch USER_ID and ACCESS_TOKEN for push messages, confirm to run the commands:')
        print('\t export LINE_USER_ID=\'USER_ID_TO_PUSH\'\)
        print('\t export LINE_ACCESS_TOKEN=\'BOT_ACCESS_TOKEN\'\)
        sys.exit(1)

    print('>>> Starting closed-loops for checking time ...')
    while True:
        if check_times_to_push:
            print('Time to notify message for user.')
            notify_to_user()
        else:
            pass