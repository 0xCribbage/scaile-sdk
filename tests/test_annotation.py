class TextAnnotation:
    """
    Handles text annotation tasks, providing methods to create and manage annotations
    for textual data.
    """

    def __init__(self, client):
        """
        Initialize the TextAnnotation class with a client instance.

        :param client: The client instance used for API communication.
        """
        self.client = client

    def create_annotation(self, text: str, labels: list):
        """
        Create a new text annotation.

        :param text: The text to be annotated.
        :param labels: A list of labels for the annotation.
        :return: Response from the API.
        """
        payload = {
            "text": text,
            "labels": labels
        }
        response = self.client.post("/annotations", json=payload)
        return response

    def get_annotation(self, annotation_id: str):
        """
        Retrieve a text annotation by its ID.

        :param annotation_id: The unique identifier of the annotation.
        :return: The annotation data.
        """
        response = self.client.get(f"/annotations/{annotation_id}")
        return response

    def update_annotation(self, annotation_id: str, labels: list):
        """
        Update an existing text annotation.

        :param annotation_id: The unique identifier of the annotation.
        :param labels: The updated list of labels.
        :return: Response from the API.
        """
        payload = {
            "labels": labels
        }
        response = self.client.put(f"/annotations/{annotation_id}", json=payload)
        return response

    def delete_annotation(self, annotation_id: str):
        """
        Delete a text annotation by its ID.

        :param annotation_id: The unique identifier of the annotation.
        :return: Response from the API.
        """
        response = self.client.delete(f"/annotations/{annotation_id}")
        return response

    def list_annotations(self, limit: int = 10, offset: int = 0):
        """
        List text annotations with pagination support.

        :param limit: The number of annotations to retrieve.
        :param offset: The starting point for retrieval.
        :return: A list of annotations.
        """
        params = {
            "limit": limit,
            "offset": offset
        }
        response = self.client.get("/annotations", params=params)
        return response