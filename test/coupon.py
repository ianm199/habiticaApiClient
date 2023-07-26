import unittest
from unittest.mock import MagicMock
from src.client import HabiticaBaseClient
from src.coupons import HabiticaCouponClient

class TestHabiticaCouponClient(unittest.TestCase):

    def setUp(self):
        self.base_client = HabiticaBaseClient("user_id", "api_key")
        self.coupon_client = HabiticaCouponClient("user_id", "api_key")

    def test_get_coupons(self):
        self.base_client.make_request = MagicMock(return_value={"coupons": []})
        response = self.coupon_client.get_coupons()
        self.assertIsInstance(response, dict)
        self.assertIn("coupons", response)

    def test_generate_coupons(self):
        event = "example_event"
        count = 5
        self.base_client.make_request = MagicMock(return_value={"success": True})
        response = self.coupon_client.generate_coupons(event, count)
        self.assertTrue(response["success"])
        self.base_client.make_request.assert_called_once_with("POST", f"/coupons/generate/{event}", params={"count": count})

    def test_redeem_coupon_code(self):
        code = "example_code"
        self.base_client.make_request = MagicMock(return_value={"success": True})
        response = self.coupon_client.redeem_coupon_code(code)
        self.assertTrue(response["success"])
        self.base_client.make_request.assert_called_once_with("POST", f"/coupons/enter/{code}")

    def test_validate_coupon(self):
        code = "example_code"
        self.base_client.make_request = MagicMock(return_value={"valid": True})
        response = self.coupon_client.validate_coupon(code)
        self.assertTrue(response["valid"])
        self.base_client.make_request.assert_called_once_with("POST", f"/coupons/validate/{code}")