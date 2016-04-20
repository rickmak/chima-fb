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


@messager_handler('chima')
def echo(payload):
    events = payload['entry'][0]['messaging']
    for evt in events:
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
            log.info('Cannot handle')

