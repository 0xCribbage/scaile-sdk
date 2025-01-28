# Contributing to Scaile SDK

Thank you for considering contributing to the Scaile SDK! Whether you’re fixing a bug, adding a new feature, or improving documentation, your contributions are always welcome. By contributing, you help make the SDK even better for everyone.

## How to Contribute

### 1. Fork the Repository

To contribute, start by forking the Scaile SDK repository to your GitHub account.

- Go to the [Scaile SDK GitHub page](https://github.com/your-repo-url).
- Click on the "Fork" button at the top right of the page.

### 2. Clone Your Fork

Once you've forked the repository, clone your fork to your local machine to make changes.

```bash
git clone https://github.com/your-username/scaile-sdk.git
cd scaile-sdk
```

### 3. Create a New Branch

Before making any changes, create a new branch to work on.

```bash
git checkout -b your-branch-name
```

### 4. Make Changes

Now you’re ready to make your changes! Be sure to follow the project’s code style and structure.

- **Bug Fixes**: If you’re fixing a bug, make sure to reference the issue number (e.g., `Fixes #123`).
- **Features**: When adding a new feature, ensure it aligns with the current structure of the SDK.
- **Documentation**: If you're improving documentation, make sure it is clear and helpful.

### 5. Write Tests

If you are adding a new feature or fixing a bug, it is important to add appropriate tests. The SDK uses [pytest](https://docs.pytest.org/en/stable/) for testing. Add your tests to the `tests/` directory.

Here’s an example of how to run tests locally:

```bash
pytest
```

### 6. Commit Your Changes

Once you're happy with your changes, commit them to your branch.

```bash
git add .
git commit -m "Your commit message"
```

Make sure your commit messages are clear and concise, describing what was changed and why.

### 7. Push Your Changes

Push your changes to your forked repository.

```bash
git push origin your-branch-name
```

### 8. Create a Pull Request

After pushing your changes, go to the Scaile SDK GitHub repository and create a pull request (PR) from your branch. In the PR description, provide a clear explanation of the changes and why they should be merged.

- Include relevant issue numbers in the PR description (e.g., `Fixes #123` or `Closes #456`).
- Provide screenshots or additional information if your PR introduces visual changes.

---

## Code Style

- **Python Version**: The SDK is built using Python 3.8 or later. Ensure that your changes are compatible with these versions.
- **PEP 8**: Please follow the Python [PEP 8](https://pep8.org/) style guide. This includes proper indentation, naming conventions, and line length.
- **Docstrings**: Add docstrings to all new classes, functions, and methods. Use [PEP 257](https://www.python.org/dev/peps/pep-0257/) conventions for docstrings.

---

## Reporting Issues

If you find a bug or have an issue with the SDK, please create an issue in the [Issues](https://github.com/your-repo-url/issues) section of the repository.

- Provide a clear description of the problem.
- Include steps to reproduce the issue.
- Add any relevant error messages or logs.

---

## License

By contributing to Scaile SDK, you agree that your contributions will be licensed under the same open-source license as the project. Please see the [LICENSE](https://github.com/your-repo-url/LICENSE) file for more details.

---

## Thank You!

We appreciate your interest in contributing to the Scaile SDK! Your efforts help make this SDK more powerful and useful for the entire community.

If you have any questions, feel free to reach out to us through issues or discussions on GitHub.

Happy coding!