from src.client import HabiticaBaseClient

class HabiticaNotificationClient(HabiticaBaseClient):
    def mark_notification_as_read(self, notification_id: str) -> dict:
        return self.make_request('POST', f'/notifications/{notification_id}/read')

    def mark_multiple_notifications_as_read(self) -> dict:
        return self.make_request('POST', '/notifications/read')

    def mark_notification_as_seen(self, notification_id: str) -> dict:
        return self.make_request('POST', f'/notifications/{notification_id}/see') 

    def mark_multiple_notifications_as_seen(self) -> dict:
        return self.make_request('POST', '/notifications/see')