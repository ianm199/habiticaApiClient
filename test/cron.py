from typing import Dict
from client import HabiticaBaseClient

class HabiticaCronClient(HabiticaBaseClient):

    def run_cron(self, data: Dict) -> dict:
        return self.make_request('POST', '/cron', data=data)

# Test cases for HabiticaCronClient

# Test run_cron method
habitica_cron_client = HabiticaCronClient(user_id, api_key)
data = {"param1": "value1", "param2": "value2"}
response = habitica_cron_client.run_cron(data)
assert response['success'] == True