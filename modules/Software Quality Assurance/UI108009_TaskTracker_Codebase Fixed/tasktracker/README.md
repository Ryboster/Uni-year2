# TaskTracker - UI108009 Assessment 2 Codebase

A simple task management REST API built with Flask and SQLite.

## Setup

```bash
pip install -r requirements.txt
python tasktracker.py
```

The API runs at `http://localhost:5001`

## Sample Users

| Username | Password  | Role  |
|----------|-----------|-------|
| admin    | admin123  | admin |
| alice    | password1 | user  |
| bob      | letmein   | user  |

## API Endpoints

| Method | Endpoint                      | Description         |
|--------|-------------------------------|---------------------|
| POST   | /api/login                    | Authenticate        |
| GET    | /api/tasks                    | List all tasks      |
| GET    | /api/tasks/&lt;id&gt;         | Get single task     |
| POST   | /api/tasks                    | Create a task       |
| PUT    | /api/tasks/&lt;id&gt;         | Update a task       |
| DELETE | /api/tasks/&lt;id&gt;         | Delete a task       |
| GET    | /api/tasks/&lt;id&gt;/comments| Get task comments   |
| POST   | /api/tasks/&lt;id&gt;/comments| Add a comment       |
| GET    | /api/users                    | List users          |
| GET    | /api/search?q=&lt;term&gt;    | Search tasks        |

## Running Tests

```bash
pytest tests/ -v
pytest --cov=tasktracker tests/ -v
```

## Your Task

See the UI108009 Assessment 2 brief for full instructions on what
to do with this codebase.
