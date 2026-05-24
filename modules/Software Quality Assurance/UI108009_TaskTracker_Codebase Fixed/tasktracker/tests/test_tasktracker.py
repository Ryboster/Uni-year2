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
    def test_post_correct_login_credentials_succeeds(self, client):
        ''' Verify /login returns correct object on successful login '''
        ### ARRANGE
        username = "admin"
        password = "admin123"

        ### ACT
        response = client.post("/api/login", json={"username": username,
                                                   "password": password})
        
        ### ASSERT
        assert len(response.get_json()) == 4
    
    def test_post_incorrect_login_credentials_fails(self, client):
        ''' Verify /login returns correct object on unsuccessful login '''
        ### ARRANGE
        username = "alice1"
        password = "1221"
        
        ### ACT
        response = client.post("/api/login", json={"username": username,
                                                   "password": password})

        ### ASSERT
        assert "error" in response.get_json()

    def test_post_incorrect_login_values_returns_valid_http_error_code(self, client):
        ''' Verify /login returns valid http responses when given incorrect values '''
        ### ARRANGE
        test_cases = [
            {"username": "", "password": ""},
            {"username": " ", "password": " "},
        ]

        for case in test_cases:
            ### ACT
            response = client.post("/api/login", json=case)

            ### ASSERT
            assert response.status_code in [400, 401]


class TestCreateTask:

    def test_post_tasks_correct_payload_succeeds(self, client):
        ''' Verify that tasks can be created '''
        # ARRANGE 
        payload = {"title": "Fix UI",
                   "description": "make big button small",
                   "priority": 3,
                   "assigned_to": "",
                   "created_by": ""}

        # ACT
        response = client.post("/api/tasks", json=payload)

        # ASSERT
        assert response.status_code == 201

    
        
    def test_post_tasks_incorrect_payload_fails(self, client):
        ''' Very that incorrect tasks are not created '''
        # ARRANGE 
        payload = {}

        # ACT
        response = client.post("/api/tasks", json=payload)

        # ASSERT
        assert response.status_code == 400
        

    def test_post_tasks_extreme_payload_fails(self, client):
        ''' Verify that extreme values are rejected '''
        # ARRANGE 
        payload = {"title": "llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll",
                   "description": "$$__`~124\\",
                   "priority": 50,
                   "assigned_to": "",
                   "created_by": ""
                   }

        # ACT
        response = client.post("/api/tasks", json=payload)

        # ASSERT
        assert response.status_code == 401


class TestGetTask:

    def test_get_task_correct_id_succeeds(self, client):
        ''' Verify that tasks can be retrieved '''
        # ARRANGE 
        task_id = 3

        # ACT
        response = client.get(f"/api/tasks/{task_id}")

        # ASSERT
        print(response.get_json())
        assert len(response.get_json()) == 8

    def test_get_invalid_id_returns_error_code(self, client):
        ''' Verify that wrong ID type returns 404 '''
        # ARRANGE 
        task_id = "one"

        # ACT
        response = client.get(f"/api/tasks/{task_id}")

        # ASSERT
        print(response.get_json())
        assert response.status_code == 404

    def test_get_edge_case_id_succeeds(self,client):
        ''' Verify that values at the edge of prohibited values are retrievable '''
        ### ARRANGE
        all_tasks = client.get("/api/tasks")
        max_valid_id = 0
        for task in all_tasks.get_json():
            if task["id"] > max_valid_id:
                max_valid_id = task["id"]

        min_valid_id = 1

        ### Act + Assert (HIGHEST case)
        response = client.get(f"/api/tasks/{max_valid_id}")
        assert len(response.get_json()) == 8

        ### Act + Assert (LOWEST case)
        response = client.get(f"/api/tasks/{min_valid_id}")
        assert len(response.get_json()) == 8


