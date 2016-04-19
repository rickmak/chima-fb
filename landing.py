import os
import requests
import skygear

from .fb import FacebookBot

oursky_fb = FacebookBot(
    '31563091484',
    os.getenv('OURSKY_TOKEN')
)


def oursky_welcome():
    message = {
        "title": """Want us to design your app idea or develop your own
        messenger bot? We’re here to help!""",
        "subtitle": "Welcome to Oursky! How may we help today?",
        "image_url": "https://oursky.com/img/logo-square.png",
        "item_url": "https://oursky.com",
        "buttons": [
            {
                "payload": "web_or_app",
                "title": "Design a web / mobile app",
                "type": "postback"
            },
            {
                "payload": "message_bot",
                "title": "Build a Messenger Bot",
                "type": "postback"
            },
            {
                "payload": "other_enquiry",
                "title": "Other development enquiry",
                "type": "postback"
            }
        ]
    }
    oursky_fb.call_to_actions(message)
