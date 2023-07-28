from src.client import HabiticaBaseClient
import requests
from typing import Optional, Dict

class HabiticaContentClient(HabiticaBaseClient):
    def get_all_available_content_objects(self, language: str = 'en') -> Dict:
        return self.make_request('GET', '/content', params={'language': language})