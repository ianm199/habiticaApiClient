from typing import Dict
from src.client import HabiticaBaseClient

class HabiticaCronClient(HabiticaBaseClient):

    def run_cron(self, data: Dict) -> dict:
        return self.make_request('POST', '/cron', data=data)