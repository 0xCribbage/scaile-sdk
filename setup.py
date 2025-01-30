from setuptools import setup, find_packages

setup(
    name='scaile-sdk',  # The name of the package
    version='0.1.0',  # The initial version of the SDK
    description='A Python SDK for interacting with the Scaile API',
    long_description=open('README.md').read(),  # Long description from the README file
    long_description_content_type='text/markdown',
    author='Scaile SDK Team',
    author_email='team@scaile.com',  # Change this to the appropriate contact email
    url='https://github.com/your-repo-url/scaile-sdk',  # The URL of the repository
    packages=find_packages(),  # Automatically find packages in the current directory
    install_requires=[
        'requests',  # List of dependencies that need to be installed
        'flask',  # If you're using Flask or any other dependencies
        'pyyaml',  # Example
        'python-dotenv',
        'pyyaml'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
    ],
    python_requires='>=3.8',  # Ensure the SDK works with Python 3.8 and above
    include_package_data=True,  # Include additional files (e.g., documentation, licenses)
    zip_safe=False,  # If you want the package to be used without extraction
)
