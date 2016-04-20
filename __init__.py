import os
import logging
import json

import requests

from .landing import oursky_welcome
from .fb import messager_handler

FB_VERIFY = os.getenv('FB_VERIFY')
CHIMA_TOKEN = os.getenv('CHIMA_TOKEN')  # recipient id 485312118265263
OURSKY_TOKEN = os.getenv('OURSKY_TOKEN')  # recipient id 31563091484

log = logging.getLogger(__name__)

# Init the facebook landing
oursky_welcome()


@messager_handler('chima', recipient_id=485312118265263)
def echo(evt):
    sender = evt['sender']['id']
    if 'message' in evt:
        msg = evt['message']
        r = requests.post(
            'https://graph.facebook.com/v2.6/me/messages',
            params={
                'access_token': CHIMA_TOKEN
            },
            json={
                'recipient': {
                    'id': sender
                },
                'message': {
                    'text': msg['text']
                }
            }
        )
        log.info(r.json())
    else:
        log.info('Cat cannot handle')


@messager_handler('chima')
def none_here(evt):
    sender = evt['sender']['id']
    if 'message' in evt:
        msg = evt['message']
        r = requests.post(
            'https://graph.facebook.com/v2.6/me/messages',
            params={
                'access_token': OURSKY_TOKEN
            },
            json={
                'recipient': {
                    'id': sender
                },
                'message': {
                    'text': 'Please email to info@oursky.com'
                }
            }
        )
        log.info(r.json())
    else:
        log.info('Cat cannot handle')
