# scaile/__init__.py

"""
scaile SDK: A Python SDK for interacting with the Scaile API.

This package provides modules for managing annotations, decentralized storage,
rewards, and utilities. Import the main `Client` class to start using the SDK.
"""

from .client import Client
from .annotation import Annotation
from .storage import Storage
from .rewards import Rewards
from .utils import Utils

__all__ = ["Client", "Annotation", "Storage", "Rewards", "Utils"]