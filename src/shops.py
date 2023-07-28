from src.client import HabiticaBaseClient
import requests
from typing import Optional, Dict

class HabiticaShopsClient(HabiticaBaseClient):
    def get_market_items(self) -> Dict:
        return self.make_request('GET', '/shops/market')

    def get_market_gear(self) -> Dict:
        return self.make_request('GET', '/shops/market-gear')

    def get_quest_shop_items(self) -> Dict:
        return self.make_request('GET', '/shops/quests')

    def get_time_travelers_shop_items(self) -> Dict:
        return self.make_request('GET', '/shops/time-travelers')

    def get_seasonal_shop_items(self) -> Dict:
        return self.make_request('GET', '/shops/seasonal')

    def get_backgrounds_shop_items(self) -> Dict:
        return self.make_request('GET', '/shops/backgrounds')