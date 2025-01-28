class Rewards:
    """
    Manages contributor reward systems, such as calculating and distributing token rewards.
    """

    def __init__(self, client):
        """
        Initializes the Rewards class with a reference to the main Client.

        :param client: An instance of the Client class for making API requests.
        """
        self.client = client

    def calculate_rewards(self, project_id: str, contributor_id: str):
        """
        Calculates rewards for a specific contributor in a project.

        :param project_id: The ID of the project.
        :param contributor_id: The ID of the contributor.
        :return: Dictionary containing reward details (e.g., tokens earned).
        """
        endpoint = f"/projects/{project_id}/contributors/{contributor_id}/rewards/calculate"
        return self.client._make_request("GET", endpoint)

    def distribute_rewards(self, project_id: str, distribution_data: dict):
        """
        Distributes rewards to contributors in a project.

        :param project_id: The ID of the project.
        :param distribution_data: Dictionary containing distribution details (e.g., contributor IDs, amounts).
        :return: Response indicating success or failure of the distribution.
        """
        endpoint = f"/projects/{project_id}/rewards/distribute"
        return self.client._make_request("POST", endpoint, json=distribution_data)

    def get_contributor_rewards(self, project_id: str, contributor_id: str):
        """
        Retrieves the reward history for a specific contributor in a project.

        :param project_id: The ID of the project.
        :param contributor_id: The ID of the contributor.
        :return: List of reward transactions for the contributor.
        """
        endpoint = f"/projects/{project_id}/contributors/{contributor_id}/rewards"
        return self.client._make_request("GET", endpoint)

    def list_all_rewards(self, project_id: str, filters: dict = None):
        """
        Retrieves a list of all rewards in a project, optionally filtered.

        :param project_id: The ID of the project.
        :param filters: Optional dictionary containing filter parameters (e.g., date range).
        :return: List of rewards.
        """
        endpoint = f"/projects/{project_id}/rewards"
        return self.client._make_request("GET", endpoint, params=filters)
