# linebot-routine-pusher

- Simple LINE bot reminders for daily basis using Python.
  - Using `LINE Messaging API` and implementation of Push notifications

- This programs intends to remind some tasks in daily basis, such as:  
  - Times of dog walking in morning / afternoon / night
  - Times when you should take some medicine
  - ...etc

***

## Environments

```text
Python : 3.6.4
pyenv : 1.2.15
line-bot-sdk : 1.15.0
```

***

## Pre-requirements

- Install required packages
  - `pip3 install -r requirements.txt`
  - or just execute `pip3 install line-bot-sdk`
  - In case if you use `pyenv` for independent package managements in the repository, run `python -m venv YOUR_ENV_NAME` first.

- Add LINE bot as your LINE friends
  - To receive push message from the bot, you shold add the bot as LINE friends.
  - There are some ways to add bot to your friends:
    - Register with QR codes
    - Register with LINE-ID
  - Notice that this is the pre-requirements by default with using LINE.

## Getting message from the bot

- Before running the programs on your environments, you should configure the parameters to allow the programs to determine the target channel.
  - For ensure security, the parameters should be retrieved from environmental variables on your machine or servers.

- Set environmental variables: `LINE_ACCESS_TOKEN` and `LINE_USER_ID`
  - `LINE_ACCESS_TOKEN`
    - An identifer for determine which bot should be run on the providers
  - `LINE_USER_ID`
    - The user ID to push message
    - Note that this ID is different from LINE ID for exchanging your account with your friend.
      - You can check the provider settings on LINE Developers account <https://developers.line.biz>
  - Again, be sure to store these parameters as environmental variables instead of hard-coding on your programs.

- Run programs on any environments
  - `python3 run.py`
    - For `virtualenv`, `source YOUR_ENV_NAME/bin/activate ; python3 ./run.py`
  - Check push notifications from the accounts reached

- If you'd like to run this programs permanently, you can simply run with OS functionalities:
  - `nohup python3 run.py &`

***

## Licensing

- As source of this program `line-bot-sdk` aligns to Apache 2.0 Licenses, all of source codes in this repository would do same as the source.
  - Souce codes in this repository are licensed under the Apache License 2.0
