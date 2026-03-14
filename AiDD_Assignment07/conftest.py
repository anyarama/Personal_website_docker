"""Pytest fixtures for the portfolio site."""

import pytest

from app import app as flask_app


@pytest.fixture(scope="session")
def app():
    """Create and configure a Flask app instance for testing."""
    flask_app.config.update(
        {
            "TESTING": True,
            "SECRET_KEY": "test-secret-key",
        }
    )
    yield flask_app


@pytest.fixture(scope="function")
def client(app):
    """Create a test client for the Flask app."""
    return app.test_client()
