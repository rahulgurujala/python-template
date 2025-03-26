"""
Sample test file to verify pytest setup.
"""

import pytest


def test_sample() -> None:
    """Basic test to verify pytest is working."""
    assert True


def test_import() -> None:
    """Test that we can import from our project."""
    try:
        import src  # noqa: F401 - Import is being tested
        assert True
    except ImportError:
        # If you don't have a package yet, this test will be skipped
        pytest.skip("src package not found")


def test_core_functions() -> None:
    """Test core functions if they exist."""
    try:
        from src.core import process_data

        result = process_data({"test": "data"})
        assert isinstance(result, dict)
        assert result.get("processed") is True
    except ImportError:
        pytest.skip("src.core module not found")
