from client import HabiticaBaseClient

class HabiticaUserClient(HabiticaBaseClient):
    def cast_spell(self, spellId: str, targetId: str = None) -> Dict:
        params = {}
        if targetId:
            params['targetId'] = targetId

        return self.make_request('POST', f'/user/class/cast/{spellId}', params=params)