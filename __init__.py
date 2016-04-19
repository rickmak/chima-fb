import os
import logging
import json

import requests
import skygear

from .landing import oursky_welcome


FB_VERIFY = os.getenv('FB_VERIFY')
CHIMA_TOKEN = os.getenv('CHIMA_TOKEN')  # recipient id 485312118265263
OURSKY_TOKEN = os.getenv('OURSKY_TOKEN')  # recipient id 31563091484

log = logging.getLogger(__name__)

# Init the facebook landing
oursky_welcome()


@skygear.handler('chima')
def verify(request, method=['GET']):
    if request.values.get('hub.verify_token') == FB_VERIFY:
        return request.values.get('hub.challenge')
    else:
        return 'You are not facebook'


@skygear.handler('chima')
def echo(request, method=['POST']):
    log.info('Got message from facebook')
    body = request.get_data(as_text=True)
    payload = json.loads(body)
    log.info(payload)
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

