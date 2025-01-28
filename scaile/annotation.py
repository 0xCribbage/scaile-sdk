class Annotation:
    """
    Handles all data annotation-related functions, such as creating, updating, and retrieving annotations.
    """

    def __init__(self, client):
        """
        Initializes the Annotation class with a reference to the main Client.

        :param client: An instance of the Client class for making API requests.
        """
        self.client = client

    def create_annotation(self, project_id: str, data: dict):
        """
        Creates a new annotation for a specific project.

        :param project_id: The ID of the project.
        :param data: Dictionary containing annotation details.
        :return: Response containing the created annotation details.
        """
        endpoint = f"/projects/{project_id}/annotations"
        return self.client._make_request("POST", endpoint, json=data)

    def get_annotation(self, project_id: str, annotation_id: str):
        """
        Retrieves a specific annotation by its ID.

        :param project_id: The ID of the project.
        :param annotation_id: The ID of the annotation to retrieve.
        :return: Annotation details.
        """
        endpoint = f"/projects/{project_id}/annotations/{annotation_id}"
        return self.client._make_request("GET", endpoint)

    def update_annotation(self, project_id: str, annotation_id: str, data: dict):
        """
        Updates an existing annotation.

        :param project_id: The ID of the project.
        :param annotation_id: The ID of the annotation to update.
        :param data: Dictionary containing updated annotation details.
        :return: Response containing the updated annotation details.
        """
        endpoint = f"/projects/{project_id}/annotations/{annotation_id}"
        return self.client._make_request("PUT", endpoint, json=data)

    def delete_annotation(self, project_id: str, annotation_id: str):
        """
        Deletes a specific annotation by its ID.

        :param project_id: The ID of the project.
        :param annotation_id: The ID of the annotation to delete.
        :return: Response indicating success or failure of deletion.
        """
        endpoint = f"/projects/{project_id}/annotations/{annotation_id}"
        return self.client._make_request("DELETE", endpoint)

    def list_annotations(self, project_id: str, filters: dict = None):
        """
        Retrieves a list of annotations for a specific project, optionally filtered.

        :param project_id: The ID of the project.
        :param filters: Optional dictionary containing filter parameters.
        :return: List of annotations.
        """
        endpoint = f"/projects/{project_id}/annotations"
        return self.client._make_request("GET", endpoint, params=filters)
