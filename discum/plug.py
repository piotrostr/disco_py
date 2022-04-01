import os

import requests


class Plug:
    def __init__(self):
        self.url = os.environ.get("PLUG_URL")
        self.api_key = os.environ.get("PLUG_KEY")
        self.asdf = ""

    def hello(self):
        res = requests.get(
            f"{self.url}/",
            headers={"Authorization": self.api_key, "Accept": "application/json"},
        )
        return res.text

    def get_user(self):
        res = requests.get(
            f"{self.url}/user",
            headers={"Authorization": self.api_key, "Accept": "application/json"},
        )
        return res.json()

    def return_user(self, user):
        res = requests.post(
            f"{self.url}/user/return",
            headers={"Authorization": self.api_key, "Content-Type": "application/json"},
            json=user,
        )
        return res.status_code
