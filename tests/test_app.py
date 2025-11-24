"""Tests for the FastAPI application"""

import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


class TestMainEndpoints:
    """Test cases for main application endpoints"""

    def test_get_activities(self):
        """Test getting all activities"""
        response = client.get("/activities")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, dict)
        assert "Chess Club" in data

    def test_genai_status(self):
        """Test GenAI status endpoint"""
        response = client.get("/genai/status")
        assert response.status_code == 200
        data = response.json()
        assert "enabled" in data
        assert isinstance(data["enabled"], bool)
