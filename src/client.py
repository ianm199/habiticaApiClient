import requests
from typing import Dict

class HabiticaBaseClient:
    def __init__(self, api_user: str, api_key: str, base_url: str = 'https://habitica.com/api/v3'):
        self.api_user = api_user
        self.api_key = api_key
        self.base_url = base_url

    def make_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.base_url}{endpoint}"
        headers = {'x-api-user': self.api_user, 'x-api-key': self.api_key}

        response = requests.request(method, url, headers=headers)

        response.raise_for_status()
        return response.json()['data']

    def bug_report(self, text: str) -> Dict:
        return self.make_request('POST', '/user/messages', json={"text": text})

    def status(self) -> Dict:
        return self.make_request('GET', '/status')

    @staticmethod
    def clean_json_input(input_dict: Dict) -> Dict:
        """Remove keys where the value is None from a dictionary"""
        return {k: v for k, v in input_dict.items() if v is not None}