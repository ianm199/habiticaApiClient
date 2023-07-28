from src.client import HabiticaBaseClient

class HabiticaNewsClient(HabiticaBaseClient):

    def get_news(self) -> dict:
        return self.make_request('GET', '/news')

    def news_tell_me_later(self) -> dict:
        return self.make_request('POST', '/news/tell-me-later')