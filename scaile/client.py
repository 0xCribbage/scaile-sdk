from .logging import logger
import requests

class Client:
    """
    The main client for interacting with the Scaile API.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.scaile.com"):
        """
        Initializes the client with authentication and base URL.

        :param api_key: API key for authentication.
        :param base_url: Base URL for the Scaile API.
        """
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def make_request(self, endpoint, payload):
        logger.debug(f"Sending request to {endpoint} with payload: {payload}")

        try:
            response = self.session.post(endpoint, json=payload)
            response.raise_for_status()
            logger.info(f"Successful response from {endpoint}")
            return response.json()
        except Exception as e:
            logger.error(f"Error during API call to {endpoint}: {str(e)}")
            raise


    def authenticate(self):
        """
        Verifies that the API key is valid.

        :return: Authentication status as a boolean.
        """
        endpoint = "/auth/validate"
        response = self._make_request("GET", endpoint)
        return response.get("valid", False)

    def get_projects(self):
        """
        Retrieves a list of projects available in the Scaile account.

        :return: List of projects.
        """
        endpoint = "/projects"
        return self._make_request("GET", endpoint)

    def create_project(self, project_data: dict):
        """
        Creates a new project in Scaile.

        :param project_data: Dictionary containing project details.
        :return: Created project details.
        """
        endpoint = "/projects"
        return self._make_request("POST", endpoint, json=project_data)

    def delete_project(self, project_id: str):
        """
        Deletes a project by its ID.

        :param project_id: The ID of the project to delete.
        :return: Response indicating success or failure.
        """
        endpoint = f"/projects/{project_id}"
        return self._make_request("DELETE", endpoint)

    def get_project_annotations(self, project_id: str):
        """
        Retrieves annotations for a specific project.

        :param project_id: The ID of the project.
        :return: List of annotations.
        """
        endpoint = f"/projects/{project_id}/annotations"
        return self._make_request("GET", endpoint)

    def submit_annotation(self, project_id: str, annotation_data: dict):
        """
        Submits an annotation for a specific project.

        :param project_id: The ID of the project.
        :param annotation_data: Dictionary containing annotation details.
        :return: Details of the submitted annotation.
        """
        endpoint = f"/projects/{project_id}/annotations"
        return self._make_request("POST", endpoint, json=annotation_data)