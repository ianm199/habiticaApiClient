from client import HabiticaBaseClient
import requests
from typing import Dict, Optional

class HabiticaCouponClient(HabiticaBaseClient):

    def get_coupons(self) -> Dict:
        return self.make_request('GET', '/coupons')

    def generate_coupons(self, event: str, count: int) -> Dict:
        return self.make_request('POST', f'/coupons/generate/{event}', params={"count": count})

    def redeem_coupon_code(self, code: str) -> Dict:
        return self.make_request('POST', f'/coupons/enter/{code}')

    def validate_coupon(self, code: str) -> Dict:
        return self.make_request('POST', f'/coupons/validate/{code}')