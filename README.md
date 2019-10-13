# notify-me

- LINEbot reminders for daily basis using Python.
  - Using `LINE Messaging API` and implementation of Push notifications

- This programs intends to remind some tasks in daily basis, such as:  
  - Times of dog walking in morning / afternoon / night
  - Times when you should take some medicine
  - ...etc

***

## Environments

```text
Python : 3.6.4
pyenv : 1.2.13
line-bot-sdk : 1.14.0
```

***

## Pre-requirements

- Install required packages
  - `pip install -r requirements.txt`
  - or just execute `pip install line-bot-sdk`

- Add LINEbot as your LINE friends
  - Use personally
    - Register with QR codes
    - Register with LINE-ID
  - Use with multiple persons
    - Invite to your rooms/groups with QR or LINE-ID
    - You could also add LINEbot with sharing contact information if some of you have already added

## Simply run once

- Set environmental variables
  - `LINE_CHANNEL_ACCESS_TOKEN` and `LINE_USER_ID`
  - These credentials must be stored in local environments only for security reason

- Run programs on any environments
  - `python push_msg.py`
  - Check push notifications from notify-me accounts reached

***

## Licensing

- TBA
