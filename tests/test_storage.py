import unittest
from unittest.mock import MagicMock
from scaile.storage import Storage

class TestStorage(unittest.TestCase):
    """
    Unit tests for the Storage class.
    """

    def setUp(self):
        """
        Setup a mocked client instance for testing.
        """
        self.mock_client = MagicMock()
        self.storage = Storage(self.mock_client)

    def test_upload_file(self):
        """
        Test the upload_file method.
        """
        file_path = "example.txt"
        self.mock_client.post.return_value = {"status": "uploaded", "file_id": "12345"}

        response = self.storage.upload_file(file_path)

        self.mock_client.post.assert_called_once_with(
            "/storage/upload", files={"file": (file_path, open(file_path, "rb"))}
        )
        self.assertEqual(response, {"status": "uploaded", "file_id": "12345"})

    def test_get_file_metadata(self):
        """
        Test the get_file_metadata method.
        """
        file_id = "12345"
        self.mock_client.get.return_value = {"file_id": "12345", "metadata": {"size": 1024}}

        response = self.storage.get_file_metadata(file_id)

        self.mock_client.get.assert_called_once_with(f"/storage/{file_id}")
        self.assertEqual(response, {"file_id": "12345", "metadata": {"size": 1024}})

    def test_delete_file(self):
        """
        Test the delete_file method.
        """
        file_id = "12345"
        self.mock_client.delete.return_value = {"status": "deleted"}

        response = self.storage.delete_file(file_id)

        self.mock_client.delete.assert_called_once_with(f"/storage/{file_id}")
        self.assertEqual(response, {"status": "deleted"})

if __name__ == "__main__":
    unittest.main()
