import os
import unittest
from unittest.mock import MagicMock
from src.coupon import HabiticaCouponClient

class TestHabiticaCouponClient(unittest.TestCase):

    def setUp(self):
        api_key = os.getenv('HABITICA_TEST_API_KEY')
        user_id = os.getenv('HABITICA_TEST_USER_ID')
        self.coupon_client = HabiticaCouponClient(user_id, api_key)

    def test_get_coupons(self):
        self.coupon_client.make_request = MagicMock(return_value={})
        response = self.coupon_client.get_coupons()
        self.assertEqual(response, {})

    def test_generate_coupons(self):
        event = "test_event"
        count = 5
        self.coupon_client.make_request = MagicMock(return_value={})
        response = self.coupon_client.generate_coupons(event, count)
        self.assertEqual(response, {})

    def test_redeem_coupon_code(self):
        code = "test_code"
        self.coupon_client.make_request = MagicMock(return_value={})
        response = self.coupon_client.redeem_coupon_code(code)
        self.assertEqual(response, {})

    def test_validate_coupon(self):
        code = "test_code"
        self.coupon_client.make_request = MagicMock(return_value={})
        response = self.coupon_client.validate_coupon(code)
        self.assertEqual(response, {})