from client import Dict
from client import HabiticaBaseClient

class HabiticaUserClient(HabiticaBaseClient):
    def user_allocate(self, stat: str = 'str') -> Dict:
        return self.make_request('POST', '/api/v3/user/allocate', params={'stat': stat})

    def user_allocate_bulk(self, stats: Dict) -> Dict:
        return self.make_request('POST', '/api/v3/user/allocate-bulk', data={'stats': stats})

    def user_allocate_now(self) -> Dict:
        return self.make_request('POST', '/api/v3/user/allocate-now')