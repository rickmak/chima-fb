import os
import logging

import skygear

log = logging.getLogger(__name__)


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
        

    def client_wants(self, what):
        if self.what != what:
            self.what = what
            self.step = 0

    def listen(self, message):
        # Save to skygear
        self.step = self.step + 1

    def speak(self): 
        log.debug('Speaking %s %s', self.what, self.step)
        try:
            return self.questions[self.what][self.step]
        except IndexError as e:
            log.warn(e)
            return 'Please email info@oursky.com for follow up'

