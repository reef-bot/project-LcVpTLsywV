# webhook_system.py

import requests

class WebhookSystem:
    def __init__(self, webhook_url):
        self.webhook_url = webhook_url

    def send_notification(self, message):
        try:
            payload = {"content": message}
            response = requests.post(self.webhook_url, json=payload)
            response.raise_for_status()
            print("Notification sent successfully")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send notification: {e}")

# End of webhook_system.py