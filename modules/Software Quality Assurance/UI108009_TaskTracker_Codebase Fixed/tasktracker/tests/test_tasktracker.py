"""
TaskTracker - Starter Test File
================================
This file contains THREE working starter tests to show you the pattern.
Your job is to add many more tests as described in the assessment brief.

TO RUN:
    pip install pytest pytest-cov flask
    pytest --cov=tasktracker tests/ -v
"""

import pytest
import json
import os
import sys

# Add parent directory so we can import tasktracker
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from tasktracker import app, init_db, DATABASE


@pytest.fixture
def client():
    """Create a test client with a fresh database for each test."""
    app.config['TESTING'] = True

    # Use a temporary database for tests
    test_db = os.path.join(os.path.dirname(__file__), 'test_tasktracker.db')
    global DATABASE
    import tasktracker
    tasktracker.DATABASE = test_db

    # Remove old test database if it exists
    if os.path.exists(test_db):
        os.remove(test_db)

    # Initialise fresh database
    init_db()

    with app.test_client() as client:
        yield client

    # Clean up
    if os.path.exists(test_db):
        os.remove(test_db)


# ── Starter tests - these three are provided for you ───────────────

class TestGetTasks:
    """Tests for the GET /api/tasks endpoint."""

    def test_get_all_tasks_returns_200(self, client):
        """Verify that the tasks endpoint returns HTTP 200."""
        response = client.get('/api/tasks')
        assert response.status_code == 200

    def test_get_all_tasks_returns_list(self, client):
        """Verify that the response is a JSON list."""
        response = client.get('/api/tasks')
        data = json.loads(response.data)
        assert isinstance(data, list)

    def test_sample_data_is_loaded(self, client):
        """Verify that sample tasks exist after init_db."""
        response = client.get('/api/tasks')
        data = json.loads(response.data)
        assert len(data) >= 3  # We inserted at least 3 sample tasks


# ── YOUR TESTS GO BELOW ────────────────────────────────────────────
#
# You need to add tests for:
#   - Login endpoint (valid login, invalid login, edge cases)
#   - Create task (valid, missing fields, boundary values)
#   - Update task (valid, non-existent task, partial updates)
#   - Delete task
#   - Comments (add, retrieve)
#   - Search
#   - User listing
#   - Security vulnerabilities (can you write a test that proves
#     the SQL injection vulnerability exists? Then another that
#     proves your fix works?)
#
# Aim for at least 15-20 tests across different test types.
# ────────────────────────────────────────────────────────────────────

class TestLoginEndpoint:

    def positive_test(self, client):
        
    
    def negative_test(self, client):

    def boundary_test(self, client):
