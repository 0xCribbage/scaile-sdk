class Storage:
    """
    Provides methods for uploading, retrieving, and managing data on decentralized storage platforms (e.g., IPFS).
    """

    def __init__(self, client):
        """
        Initializes the Storage class with a reference to the main Client.

        :param client: An instance of the Client class for making API requests.
        """
        self.client = client

    def upload_data(self, project_id: str, file_path: str):
        """
        Uploads a file to the decentralized storage platform.

        :param project_id: The ID of the project.
        :param file_path: The local path to the file to be uploaded.
        :return: Response containing the storage location and metadata.
        """
        endpoint = f"/projects/{project_id}/storage/upload"
        with open(file_path, 'rb') as file:
            files = {"file": file}
            return self.client._make_request("POST", endpoint, files=files)

    def retrieve_data(self, project_id: str, file_id: str):
        """
        Retrieves a file from the decentralized storage platform.

        :param project_id: The ID of the project.
        :param file_id: The ID of the file to retrieve.
        :return: File content or metadata.
        """
        endpoint = f"/projects/{project_id}/storage/files/{file_id}"
        return self.client._make_request("GET", endpoint)

    def delete_data(self, project_id: str, file_id: str):
        """
        Deletes a file from the decentralized storage platform.

        :param project_id: The ID of the project.
        :param file_id: The ID of the file to delete.
        :return: Response indicating success or failure of deletion.
        """
        endpoint = f"/projects/{project_id}/storage/files/{file_id}"
        return self.client._make_request("DELETE", endpoint)

    def list_files(self, project_id: str, filters: dict = None):
        """
        Lists all files stored in a project, optionally filtered.

        :param project_id: The ID of the project.
        :param filters: Optional dictionary containing filter parameters (e.g., file type, date uploaded).
        :return: List of files and their metadata.
        """
        endpoint = f"/projects/{project_id}/storage/files"
        return self.client._make_request("GET", endpoint, params=filters)
