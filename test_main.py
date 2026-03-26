"""Tests for the FastAPI DevOps assignment app."""

from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_root_status_code():
    """Root endpoint should return 200."""
    response = client.get("/")
    assert response.status_code == 200


def test_root_contains_name():
    """Root page should display the submitter's name."""
    response = client.get("/")
    assert "Prashasst Dongre" in response.text


def test_root_contains_enrollment():
    """Root page should display the enrollment number."""
    response = client.get("/")
    assert "0201AI221053" in response.text


def test_root_contains_semester():
    """Root page should mention the semester."""
    response = client.get("/")
    assert "8th Sem" in response.text


def test_root_contains_branch():
    """Root page should mention the branch."""
    response = client.get("/")
    assert "Artificial Intelligence and Data Science" in response.text


def test_root_is_html():
    """Root endpoint should return HTML content."""
    response = client.get("/")
    assert "text/html" in response.headers["content-type"]


def test_health_endpoint():
    """Health check endpoint should return ok status."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
