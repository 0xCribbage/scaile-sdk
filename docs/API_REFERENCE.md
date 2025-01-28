# API Reference - Scaile SDK

This document provides a detailed reference of all the methods available in the Scaile SDK. It includes method descriptions, parameters, and examples of how to use each method.

---

## Client

The `Client` class is used to authenticate and interact with the Scaile API.

### `Client(api_key: str)`

#### Parameters:
- `api_key` (str): The API key used for authentication.

#### Example:
```python
from scaile.client import Client

# Create a client instance using the API key
client = Client(api_key="your_api_key")
```

### `Client.get_annotations()`

Fetches all annotations associated with the authenticated account.

#### Returns:
- List of `Annotation` objects.

#### Example:
```python
annotations = client.get_annotations()
for annotation in annotations:
    print(annotation)
```

---

## Annotation

The `Annotation` class is used for creating, updating, and retrieving annotations.

### `Annotation.create(data: dict)`

Creates a new annotation.

#### Parameters:
- `data` (dict): A dictionary containing the annotation data, such as `text` and `labels`.

#### Returns:
- An `Annotation` object representing the created annotation.

#### Example:
```python
from scaile.annotation import Annotation

data = {
    "text": "This is a new annotation",
    "labels": ["label1", "label2"]
}
annotation = Annotation.create(data)
print(f"Created annotation: {annotation}")
```

### `Annotation.get(annotation_id: str)`

Fetches an existing annotation by its ID.

#### Parameters:
- `annotation_id` (str): The ID of the annotation to retrieve.

#### Returns:
- An `Annotation` object.

#### Example:
```python
annotation = Annotation.get("annotation_id_here")
print(f"Fetched annotation: {annotation}")
```

### `Annotation.update(annotation_id: str, data: dict)`

Updates an existing annotation.

#### Parameters:
- `annotation_id` (str): The ID of the annotation to update.
- `data` (dict): A dictionary of updated data, such as new `text` or `labels`.

#### Returns:
- An `Annotation` object representing the updated annotation.

#### Example:
```python
updated_data = {
    "text": "Updated annotation text",
    "labels": ["label1", "label3"]
}
updated_annotation = Annotation.update("annotation_id_here", updated_data)
print(f"Updated annotation: {updated_annotation}")
```

### `Annotation.delete(annotation_id: str)`

Deletes an existing annotation.

#### Parameters:
- `annotation_id` (str): The ID of the annotation to delete.

#### Returns:
- `None`.

#### Example:
```python
Annotation.delete("annotation_id_here")
print("Annotation deleted")
```

---

## Storage

The `Storage` class is used for interacting with decentralized storage platforms (e.g., IPFS).

### `Storage.upload(file_path: str)`

Uploads a file to a decentralized storage platform.

#### Parameters:
- `file_path` (str): The path to the file to upload.

#### Returns:
- A URL or a storage ID for the uploaded file.

#### Example:
```python
from scaile.storage import Storage

file_url = Storage.upload("path_to_file_here")
print(f"File uploaded successfully: {file_url}")
```

### `Storage.retrieve(file_id: str)`

Retrieves a file from the decentralized storage platform.

#### Parameters:
- `file_id` (str): The ID or URL of the file to retrieve.

#### Returns:
- The content of the file.

#### Example:
```python
file_content = Storage.retrieve("file_id_here")
print(f"Retrieved file content: {file_content}")
```

---

## Rewards

The `Rewards` class is used for managing contributor rewards, including token allocation.

### `Rewards.calculate_tokens(contributor_id: str)`

Calculates the number of tokens to reward a contributor.

#### Parameters:
- `contributor_id` (str): The ID of the contributor.

#### Returns:
- The number of tokens awarded to the contributor.

#### Example:
```python
from scaile.rewards import Rewards

tokens = Rewards.calculate_tokens("contributor_id_here")
print(f"Tokens awarded: {tokens}")
```

---

## Utils

The `Utils` class provides helper functions for common tasks such as error handling and response processing.

### `Utils.handle_api_error(error: Exception)`

Handles API errors by logging the error message and taking appropriate action (e.g., retries, alerts).

#### Parameters:
- `error` (Exception): The error object to handle.

#### Returns:
- `None`.

#### Example:
```python
from scaile.utils import handle_api_error

try:
    # Example code that might raise an error
    raise ValueError("An error occurred")
except Exception as e:
    handle_api_error(e)
```

---

## Error Handling

The SDK provides built-in error handling to ensure that API interactions are properly managed. The most common error is API-related, such as invalid data or authentication issues.

### `ScaileAPIError`

An error that occurs when the API returns an invalid response. This is typically thrown when the request is malformed or when authentication fails.

#### Example:
```python
from scaile.utils import ScaileAPIError

try:
    # Example code that might raise an API error
    raise ScaileAPIError("Invalid API request")
except ScaileAPIError as e:
    print(f"API Error: {e}")
```

---

This concludes the API reference for the Scaile SDK. You can explore these methods to interact with the Scaile API and integrate its functionality into your applications.