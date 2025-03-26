"""
Shared pytest fixtures for the test suite.
"""

from typing import Any, Dict

import pytest


@pytest.fixture
def sample_fixture() -> Dict[str, Any]:
    """
    A sample fixture that can be used across tests.

    Returns:
        A sample dictionary
    """
    return {"key": "value"}
