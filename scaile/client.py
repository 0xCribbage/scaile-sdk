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

    def _make_request(self, method: str, endpoint: str, **kwargs):
        """
        Handles API requests with error handling.

        :param method: HTTP method (GET, POST, etc.).
        :param endpoint: API endpoint to target.
        :param kwargs: Additional parameters for the request (e.g., data, params).
        :return: JSON response or raises an error.
        """
        url = f"{self.base_url}{endpoint}"
        try:
            response = requests.request(method, url, headers=self.headers, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            print(f"HTTP error occurred: {e}")
            raise
        except Exception as e:
            print(f"An error occurred: {e}")
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