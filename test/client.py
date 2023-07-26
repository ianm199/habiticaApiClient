import requests
from typing import Dict, Optional

class HabiticaBaseClient:
    def __init__(self, api_user: str, api_key: str, base_url: str = 'https://habitica.com/api/v3'):
        self.api_user = api_user
        self.api_key = api_key
        self.base_url = base_url

    def make_request(self, method: str, endpoint: str, params: Optional[dict] = None, data: Optional[dict] = None) -> Dict:
        url = f"{self.base_url}{endpoint}"
        headers = {'x-api-user': self.api_user, 'x-api-key': self.api_key}
        if data:
            request_data = {}
            for key, val in data.items():
                if type(val) == bool:
                    request_data[key] = str(val).lower()
                elif val is not None:
                    request_data[key] = val
        if method == "POST" and data:
            response = requests.request(method, url, headers=headers, data=request_data)
        else:
            extra_args = {}
            if params:
                extra_args["params"] = params
            if data:
                extra_args["data"] = request_data
            response = requests.request(method, url, headers=headers, **extra_args)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Response Json:")
            print(response.json())
            raise e
        return response.json()['data']

    def bug_report(self, text: str) -> Dict:
        return self.make_request('POST', '/user/messages', data={"text": text})

    def status(self) -> Dict:
        return self.make_request('GET', '/status')

    @staticmethod
    def clean_json_input(input_dict: Dict) -> Dict:
        """Remove keys where the value is None from a dictionary"""
        return {k: v for k, v in input_dict.items() if v is not None}

# Test Case 1: Testing make_request method with GET request
client = HabiticaBaseClient("username", "api_key")
response = client.make_request("GET", "/status")
assert response['data'] is not None

# Test Case 2: Testing make_request method with POST request
client = HabiticaBaseClient("username", "api_key")
response = client.make_request("POST", "/user/messages", data={"text": "Test message"})
assert response['data'] is not None

# Test Case 3: Testing bug_report method
client = HabiticaBaseClient("username", "api_key")
response = client.bug_report("Bug description")
assert response['data'] is not None

# Test Case 4: Testing status method
client = HabiticaBaseClient("username", "api_key")
response = client.status()
assert response['data'] is not None

# Test Case 5: Testing clean_json_input method
input_dict = { "key1": "value1", "key2": None, "key3": "value3" }
clean_dict = client.clean_json_input(input_dict)
assert clean_dict == { "key1": "value1", "key3": "value3" }