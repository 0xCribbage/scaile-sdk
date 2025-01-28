import unittest
from unittest.mock import MagicMock
from scaile.rewards import Rewards

class TestRewards(unittest.TestCase):
    """
    Unit tests for the Rewards class.
    """

    def setUp(self):
        """
        Setup a mocked client instance for testing.
        """
        self.mock_client = MagicMock()
        self.rewards = Rewards(self.mock_client)

    def test_calculate_rewards(self):
        """
        Test the calculate_rewards method.
        """
        contributions = [
            {"user_id": "user1", "contribution": 10},
            {"user_id": "user2", "contribution": 20},
        ]
        self.mock_client.post.return_value = {"status": "success"}

        response = self.rewards.calculate_rewards(contributions)

        self.mock_client.post.assert_called_once_with(
            "/rewards/calculate", json={"contributions": contributions}
        )
        self.assertEqual(response, {"status": "success"})

    def test_get_user_rewards(self):
        """
        Test the get_user_rewards method.
        """
        user_id = "user1"
        self.mock_client.get.return_value = {"rewards": 100}

        response = self.rewards.get_user_rewards(user_id)

        self.mock_client.get.assert_called_once_with(f"/rewards/{user_id}")
        self.assertEqual(response, {"rewards": 100})

    def test_distribute_rewards(self):
        """
        Test the distribute_rewards method.
        """
        rewards_data = [
            {"user_id": "user1", "reward": 50},
            {"user_id": "user2", "reward": 100},
        ]
        self.mock_client.post.return_value = {"status": "distributed"}

        response = self.rewards.distribute_rewards(rewards_data)

        self.mock_client.post.assert_called_once_with(
            "/rewards/distribute", json={"rewards": rewards_data}
        )
        self.assertEqual(response, {"status": "distributed"})

if __name__ == "__main__":
    unittest.main()
