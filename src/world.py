from client import HabiticaBaseClient
from typing import Dict

class HabiticaWorldStateClient(HabiticaBaseClient):
    def get_world_state(self) -> Dict:
        return self.make_request('GET', '/world-state')