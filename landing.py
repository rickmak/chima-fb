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
        "title": """Welcome to Oursky!""",
        "subtitle": """We're a team of 40 app developers based in HK, How may we
        help you?""",
        "image_url": "https://oursky.com/img/logo-square.png",
        "item_url": "https://oursky.com",
        "buttons": [
            {
                "payload": "web_or_app",
                "title": "Design an app",
                "type": "postback"
            },
            {
                "payload": "message_bot",
                "title": "Build my FB Bot",
                "type": "postback"
            },
            {
                "payload": "other_enquiry",
                "title": "Other enquiry",
                "type": "postback"
            }
        ]
    }
    oursky_fb.call_to_actions(message)
