import os
 
from linebot import LineBotApi
from linebot.models import TextSendMessage
 
# Set credentilas securely
channel_access_token = os.getenv('LINE_CHANNEL_ACCESS_TOKEN', None)
line_user_id = os.getenv('LINE_USER_ID', None)

# Instanciate LINEBot object 
line_bot_api = LineBotApi(channel_access_token)
 
def main():
    messages = TextSendMessage(text="Hello LINE Push notifications.")
    line_bot_api.push_message(line_user_id, messages=messages)
 
if __name__ == "__main__":
    main()
