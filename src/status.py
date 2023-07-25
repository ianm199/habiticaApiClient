from typing import Dict
from client import HabiticaBaseClient


class HabiticaStatusClient(HabiticaBaseClient):
    def get_status(self) -> Dict:
        return self.make_request('GET', '/status')