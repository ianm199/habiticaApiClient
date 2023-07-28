from typing import Optional, Dict
import requests
from src.client import HabiticaBaseClient

class HabiticaHallClient(HabiticaBaseClient):
    def get_all_patrons(self, page: int = 0) -> Dict:
        return self.make_request('GET', '/hall/patrons', params={'page': page})

    def get_all_heroes(self) -> Dict:
        return self.make_request('GET', '/hall/heroes')

    def get_hero(self, heroId: str) -> Dict:
        return self.make_request('GET', f'/hall/heroes/{heroId}')

    def update_hero(self, heroId: str, data: Dict) -> Dict:
        return self.make_request('PUT', f'/hall/heroes/{heroId}', data=data)

    def get_hero_party(self, groupId: str) -> Dict:
        return self.make_request('GET', f'/hall/heroes/party/{groupId}')