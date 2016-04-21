import os
import logging
import json

import requests

from .landing import oursky_welcome
from .fb import messager_handler
from .bot import OurskyBot

CHIMA_TOKEN = os.getenv('CHIMA_TOKEN')  # recipient id 485312118265263
OURSKY_TOKEN = os.getenv('OURSKY_TOKEN')  # recipient id 31563091484

log = logging.getLogger(__name__)

# Init the facebook landing
oursky_welcome()


@messager_handler('chima', recipient_id=485312118265263, token=CHIMA_TOKEN)
def echo(evt, postman):
    sender = evt['sender']['id']
    if 'message' in evt:
        msg = evt['message']
        r = postman.message(sender, msg)
        log.info(r.json())
    else:
        log.info('Cat cannot handle')


@messager_handler('chima', recipient_id=31563091484, postback='web_or_app', token=OURSKY_TOKEN)
def web_or_app(evt, postman):
    sender = evt['sender']['id']
    bot = OurskyBot(sender)
    bot.client_wants('web_or_app')
    msg = bot.speak()
    msg = 'Can you briefly describe your idea?'
    r = postman.message(sender, msg)
    log.info(r.json())
    return 'ok'


@messager_handler('chima', recipient_id=31563091484, postback='message_bot', token=OURSKY_TOKEN)
def message_bot(evt, postman):
    sender = evt['sender']['id']
    msg = 'Interesting! Which company / business are you from?'
    bot = OurskyBot(sender)
    bot.client_wants('message_bot')
    msg = bot.speak()
    r = postman.message(sender, msg)
    log.info(r.json())
    return 'ok'


@messager_handler('chima', recipient_id=31563091484, postback='other_enquiry', token=OURSKY_TOKEN)
def other_enquiry(evt, postman):
    sender = evt['sender']['id']
    msg = 'Can you briefly describe your needs?'
    bot = OurskyBot(sender)
    bot.client_wants('other_enquiry')
    msg = bot.speak()
    r = postman.message(sender, msg)
    log.info(r.json())
    return 'ok'


@messager_handler('chima', recipient_id=31563091484, token=OURSKY_TOKEN)
def message_to_oursky(evt, postman):
    sender = evt['sender']['id']
    bot = OurskyBot(sender)
    if 'message' in evt:
        msg = evt['message']
        bot.listen(msg)
        response = bot.speak()
        r = postman.message(sender, response)
        log.info(r.json())
    else:
        log.info('Cat cannot handle')
