import unittest
from unittest.mock import MagicMock
from scaile.client import Client

class TestClient(unittest.TestCase):
    """
    Unit tests for the Client class.
    """

    def setUp(self):
        """
        Set up the test environment with a mock base URL and API key.
        """
        self.base_url = "https://api.scaile.com"
        self.api_key = "test_api_key"
        self.client = Client(base_url=self.base_url, api_key=self.api_key)

    def test_init(self):
        """
        Test the initialization of the Client class.
        """
        self.assertEqual(self.client.base_url, self.base_url)
        self.assertEqual(self.client.api_key, self.api_key)

    def test_get(self):
        """
        Test the GET request method.
        """
        self.client.session.get = MagicMock(return_value=MagicMock(status_code=200, json=lambda: {"data": "test"}))
        response = self.client.get("/test")
        self.client.session.get.assert_called_once_with(f"{self.base_url}/test", headers=self.client.headers, params=None)
        self.assertEqual(response["data"], "test")

    def test_post(self):
        """
        Test the POST request method.
        """
        self.client.session.post = MagicMock(return_value=MagicMock(status_code=201, json=lambda: {"success": True}))
        payload = {"key": "value"}
        response = self.client.post("/test", json=payload)
        self.client.session.post.assert_called_once_with(f"{self.base_url}/test", headers=self.client.headers, json=payload)
        self.assertTrue(response["success"])

    def test_put(self):
        """
        Test the PUT request method.
        """
        self.client.session.put = MagicMock(return_value=MagicMock(status_code=200, json=lambda: {"updated": True}))
        payload = {"key": "new_value"}
        response = self.client.put("/test", json=payload)
        self.client.session.put.assert_called_once_with(f"{self.base_url}/test", headers=self.client.headers, json=payload)
        self.assertTrue(response["updated"])

    def test_delete(self):
        """
        Test the DELETE request method.
        """
        self.client.session.delete = MagicMock(return_value=MagicMock(status_code=204))
        response = self.client.delete("/test")
        self.client.session.delete.assert_called_once_with(f"{self.base_url}/test", headers=self.client.headers)
        self.assertIsNone(response)

if __name__ == "__main__":
    unittest.main()