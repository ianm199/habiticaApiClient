import unittest
import unittest.mock as mock
from src.news import HabiticaNewsClient

class TestHabiticaNewsClient(unittest.TestCase):
    def setUp(self):
        self.news_client = HabiticaNewsClient("user", "api")

    def test_get_news(self):
        with mock.patch.object(self.news_client, 'make_request') as mock_make_request:
            self.news_client.get_news()
            mock_make_request.assert_called_once_with('GET', '/news')

    def test_news_tell_me_later(self):
        with mock.patch.object(self.news_client, 'make_request') as mock_make_request:
            self.news_client.news_tell_me_later()
            mock_make_request.assert_called_once_with('POST', '/news/tell-me-later')