from src.client import HabiticaBaseClient

class HabiticaPushNotifications(HabiticaBaseClient):
    
    def add_push_device(self, regId: str, type: str) -> dict:
        return self.make_request('POST', '/user/push-devices', data={"regId": regId, "type": type})

    def remove_push_device(self, regId:str) -> dict:
        return self.make_request('DELETE', f'/user/push-devices/{regId}')