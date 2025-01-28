# Scaile SDK Documentation

Welcome to the official documentation for the **Scaile SDK**! This SDK provides an easy-to-use interface for interacting with the Scaile API, offering features for annotation management, decentralized storage, contributor rewards, and more.

This documentation will help you get started with integrating the Scaile SDK into your applications, and will guide you through the setup process, key functionalities, and how to contribute to the SDK.

---

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [SDK Components](#sdk-components)
  - [Client](#client)
  - [Annotation](#annotation)
  - [Storage](#storage)
  - [Rewards](#rewards)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Scaile SDK** is a Python library designed to interact with the Scaile API. It simplifies tasks such as:

- Creating, retrieving, and updating annotations.
- Uploading and managing files on decentralized storage platforms (e.g., IPFS).
- Managing contributor rewards (e.g., calculating and distributing tokens).
- Listening for real-time notifications via webhooks.

This SDK is perfect for developers building applications that require advanced annotation management, decentralized file storage, or reward systems for contributors.

---

## Installation

To install the Scaile SDK, you can use `pip`:

1. First, ensure you have Python 3.8 or later installed.
2. Install the SDK using the following command:

```bash
pip install scaile-sdk
```

Alternatively, you can clone the repository and install the SDK manually:

```bash
git clone https://github.com/your-repo-url/scaile-sdk.git
cd scaile-sdk
pip install .
```

Additionally, you can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

---

## Getting Started

After installation, you can begin using the Scaile SDK in your Python projects. Below is an example to help you get started quickly.

### Example - Quickstart

```python
from scaile.client import Client

# Initialize the client with your API key
client = Client(api_key="your_api_key")

# Fetch all annotations
annotations = client.get_annotations()

for annotation in annotations:
    print(annotation)
```

This example demonstrates how to authenticate using the API key and retrieve annotations from the Scaile platform.

---

## SDK Components

The Scaile SDK is composed of several key components:

### Client

The `Client` class provides an interface for interacting with the Scaile API. It handles authentication, session management, and API requests.

#### Key Methods:
- `get_annotations()`: Fetches all annotations.
- `create_annotation(data)`: Creates a new annotation.
- `get_annotation_by_id(annotation_id)`: Retrieves a specific annotation by ID.

### Annotation

The `Annotation` class handles all functions related to data annotations.

#### Key Methods:
- `create(data)`: Creates a new annotation.
- `update(annotation_id, data)`: Updates an existing annotation.
- `delete(annotation_id)`: Deletes an annotation.

### Storage

The `Storage` class provides methods for interacting with decentralized storage platforms like IPFS.

#### Key Methods:
- `upload(file_path)`: Uploads a file to a decentralized platform.
- `retrieve(file_id)`: Retrieves a file from the storage.

### Rewards

The `Rewards` class manages the reward system, such as calculating tokens for contributors.

#### Key Methods:
- `calculate_tokens(contributor_id)`: Calculates the number of tokens to reward a contributor.
- `distribute_rewards()`: Distributes rewards to eligible contributors.

---

## API Reference

For detailed information on how to use the SDK's classes and methods, please refer to the [API Reference](API_REFERENCE.md).

---

## Contributing

We welcome contributions to the Scaile SDK! If you’d like to contribute, please check out the [Contributing Guide](CONTRIBUTING.md) for instructions on how to get started.

---

## License

The Scaile SDK is open-source and licensed under the [MIT License](https://github.com/your-repo-url/LICENSE).

---

Thank you for using the Scaile SDK! We hope it enhances your development experience and helps you build amazing applications. If you have any questions or need further assistance, feel free to reach out to us via issues on GitHub.

Happy coding!