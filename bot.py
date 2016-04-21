import os
import logging
import uuid

from skygear.container import SkygearContainer
from skygear.error import SkygearException

log = logging.getLogger(__name__)

skygear_token = None


def get_token():
    global skygear_token
    if skygear_token is not None:
        return skygear_token

    container = SkygearContainer()
    try:
        resp = container.send_action('auth:login', {
            'username': os.getenv('SKYGEAR_BOT'),
            'password': os.getenv('SKYGEAR_BOT_PW')
        })
    except SkygearException:
        log.debug('New setup, registering')
        resp = container.send_action('auth:signup', {
            'username': os.getenv('SKYGEAR_BOT'),
            'password': os.getenv('SKYGEAR_BOT_PW')
        })
    finally:
        log.debug(resp)
        skygear_token = resp['result']['access_token']
    return skygear_token

class OurskyBot():
    questions = {
        'chat': [
            'What free chat?, email info@oursky.com'
        ],
        'web_or_app': [
            'Can you briefly describe your idea?',
            'Which email shall our Project Consultant reach you at?',
            'Great! Thank you and we will be in touch shortly.!',
#    * Learn more about Oursky prototyping services (button, url to
#                                                    https://oursky.com/prototype/)
        ],
        'message_bot': [
            'Interesting! Which company / business are you from?',
            'How do you plan to use Messenger Bot?',
            'Interesting! Which email shall we reach you?',
            'Thanks! We will be in touch short!',
#    * Learn more about Oursky (button, url to oursky.com (http://oursky.com/))
        ],
        'other_enquiry': [
            'Can you briefly describe your needs?',
            'What is your company name?',
            'Which email shall our Project Consultant reach you at?',
            'Great! Thank you and we will be in touch shortly!',
#    * Learn more about Oursky (button, url to oursky.com (http://oursky.com/))
        ]
    }

    def __init__(self, user):
        self.what = 'chat'
        self.step = 0
        self.user = user
        self.container = SkygearContainer(access_token=get_token())
        response = self.container.send_action('record:query', {
            'record_type': 'fb_user',
            'predicate': [
                'eq',
                {'$type': 'keypath', '$val': '_id'},
                user 
            ]
        })
        log.debug(response)
        result = response['result']
        user = result[0]
        if user:
            self.step = user['step']
            self.what = user['enquiry_topic']

    def client_wants(self, what):
        if self.what != what:
            self.what = what
            self.step = 0
            self.upsert_fb_user()

    def upsert_fb_user(self):
        self.container.send_action('record:save', {'records': [{
            '_id': 'fb_user/{}'.format(self.user),
            'enquiry_topic': self.what,
            'step': self.step
        }]})

    def listen(self, message):
        # Save to skygear
        self.step = self.step + 1
        self.upsert_fb_user()
        self.container.send_action('record:save', {'records': [{
            '_id': 'fb_message/{}'.format(uuid.uuid4()),
            'enquiry_topic': self.what,
            'message': message
        }]})

    def speak(self): 
        log.debug('Speaking %s %s', self.what, self.step)
        try:
            return self.questions[self.what][self.step]
        except IndexError as e:
            log.warn(e)
            return 'Please email info@oursky.com for follow up'

