import logging
import requests

log = logging.getLogger(__name__)


class FacebookBot():
    def __init__(self, page_id, token):
        self.page_id = page_id
        self.token = token

    @property
    def thread_settings_url(self):
        url = "https://graph.facebook.com/v2.6/{page_id}/thread_settings"
        return url.format(page_id=self.page_id)

    def call_to_actions(self, message):
        r = requests.post(
            self.thread_settings_url,
            params={
                'access_token': self.token
            },
            json={
                "call_to_actions": [{
                    "message": {
                        "attachment": {
                            "payload": {
                                "template_type": "generic",
                                "elements": [message]
                            },
                            "type": "template"
                        }
                    }
                }],
                "setting_type": "call_to_actions",
                "thread_state": "new_thread"
            }
        )
        log.info(r.json())
