"""
TaskTracker - A Simple Task Management API
==========================================
UI108009 Software Quality Assurance - Assessment 2

This application is provided for your Verification and Testing Report.
It is a working Flask API for managing tasks in a team.

TO RUN:
    pip install flask
    python tasktracker.py

The API will be available at http://localhost:5001

ENDPOINTS:
    POST   /api/login                  - Authenticate
    GET    /api/tasks                  - List all tasks
    GET    /api/tasks/<id>             - Get one task
    POST   /api/tasks                  - Create a task
    PUT    /api/tasks/<id>             - Update a task
    DELETE /api/tasks/<id>             - Delete a task
    GET    /api/tasks/<id>/comments    - Get task comments
    POST   /api/tasks/<id>/comments    - Add a comment
    GET    /api/users                  - List users
    GET    /api/search?q=<term>        - Search tasks
"""

import sqlite3
import os
import hashlib
from flask import Flask, request, jsonify, g, render_template_string

app = Flask(__name__)
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tasktracker.db')


# ── Database ────────────────────────────────────────────────────────

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()


def init_db():
    """Create tables and insert sample data."""
    db = sqlite3.connect(DATABASE)

    db.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        email TEXT,
        role TEXT DEFAULT 'user'
    )''')

    db.execute('''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT DEFAULT 'todo',
        priority INTEGER DEFAULT 3,
        assigned_to INTEGER,
        created_by INTEGER,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (assigned_to) REFERENCES users(id),
        FOREIGN KEY (created_by) REFERENCES users(id)
    )''')

    db.execute('''CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id INTEGER NOT NULL,
        user_id INTEGER,
        content TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (task_id) REFERENCES tasks(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )''')

    count = db.execute("SELECT COUNT(*) FROM users").fetchone()[0]
    if count == 0:
        db.execute(
            "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
            ("admin", hashlib.md5("admin123".encode()).hexdigest(),
             "admin@tasktracker.local", "admin"))
        db.execute(
            "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
            ("alice", hashlib.md5("password1".encode()).hexdigest(),
             "alice@company.com", "user"))
        db.execute(
            "INSERT INTO users (username, password, email, role) VALUES (?,?,?,?)",
            ("bob", hashlib.md5("letmein".encode()).hexdigest(),
             "bob@company.com", "user"))

        db.execute(
            "INSERT INTO tasks (title, description, status, priority, assigned_to, created_by) "
            "VALUES (?,?,?,?,?,?)",
            ("Fix login page CSS",
             "The login button is misaligned on mobile devices",
             "todo", 2, 2, 1))
        db.execute(
            "INSERT INTO tasks (title, description, status, priority, assigned_to, created_by) "
            "VALUES (?,?,?,?,?,?)",
            ("Add password reset feature",
             "Users need the ability to reset their password via email",
             "in_progress", 1, 3, 1))
        db.execute(
            "INSERT INTO tasks (title, description, status, priority, assigned_to, created_by) "
            "VALUES (?,?,?,?,?,?)",
            ("Write API documentation",
             "The Swagger docs are out of date and need refreshing",
             "todo", 3, 2, 1))
        db.execute(
            "INSERT INTO tasks (title, description, status, priority, assigned_to, created_by) "
            "VALUES (?,?,?,?,?,?)",
            ("Database backup automation",
             "Set up automated daily backups of the production database",
             "todo", 1, 3, 1))
        db.execute(
            "INSERT INTO tasks (title, description, status, priority, assigned_to, created_by) "
            "VALUES (?,?,?,?,?,?)",
            ("Refactor user service",
             "The user service module has grown too large and needs splitting",
             "in_progress", 2, 2, 1))

    db.commit()
    db.close()


# ── Authentication ──────────────────────────────────────────────────

@app.route('/api/login', methods=['POST'])
def login():
    """Authenticate a user and return their details."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    username = data.get('username', '')
    password = data.get('password', '')
    password_hash = hashlib.md5(password.encode()).hexdigest()

    db = get_db()

    # Build query using string formatting
    query = "SELECT * FROM users WHERE username = '{}' AND password = '{}'".format(
        username, password_hash
    )
    user = db.execute(query).fetchone()

    if user:
        return jsonify({
            "message": "Login successful",
            "user_id": user['id'],
            "username": user['username'],
            "role": user['role']
        })
    return jsonify({"error": "Invalid credentials"}), 401


# ── Tasks ───────────────────────────────────────────────────────────

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """Return all tasks ordered by priority."""
    db = get_db()
    tasks = db.execute(
        "SELECT * FROM tasks ORDER BY priority ASC"
    ).fetchall()
    return jsonify([dict(t) for t in tasks])


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Return a single task."""
    db = get_db()
    task = db.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    if task:
        return jsonify(dict(task))
    return jsonify({"error": "Task not found"}), 404


@app.route('/api/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body required"}), 400

    title = data.get('title', '')
    description = data.get('description', '')
    priority = data.get('priority', 3)
    assigned_to = data.get('assigned_to')
    created_by = data.get('created_by', 1)

    db = get_db()
    cursor = db.execute(
        "INSERT INTO tasks (title, description, priority, assigned_to, created_by) "
        "VALUES (?, ?, ?, ?, ?)",
        (title, description, priority, assigned_to, created_by)
    )
    db.commit()
    return jsonify({"id": cursor.lastrowid, "message": "Task created"}), 201


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    """Update an existing task."""
    data = request.get_json()
    db = get_db()

    task = db.execute(
        "SELECT * FROM tasks WHERE id = ?", (task_id,)
    ).fetchone()
    if not task:
        return jsonify({"error": "Task not found"}), 404

    title = data.get('title', task['title'])
    description = data.get('description', task['description'])
    status = data.get('status', task['status'])
    priority = data.get('priority', task['priority'])

    db.execute(
        "UPDATE tasks SET title=?, description=?, status=?, priority=? WHERE id=?",
        (title, description, status, priority, task_id)
    )
    db.commit()
    return jsonify({"message": "Task updated"})


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    """Delete a task."""
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return jsonify({"message": "Task deleted"})


# ── Comments ────────────────────────────────────────────────────────

@app.route('/api/tasks/<int:task_id>/comments', methods=['GET'])
def get_comments(task_id):
    """Return all comments for a task."""
    db = get_db()
    comments = db.execute(
        "SELECT * FROM comments WHERE task_id = ? ORDER BY created_at ASC",
        (task_id,)
    ).fetchall()
    return jsonify([dict(c) for c in comments])


@app.route('/api/tasks/<int:task_id>/comments', methods=['POST'])
def add_comment(task_id):
    """Add a comment to a task."""
    data = request.get_json()
    content = data.get('content', '')
    user_id = data.get('user_id', 1)

    db = get_db()
    cursor = db.execute(
        "INSERT INTO comments (task_id, user_id, content) VALUES (?, ?, ?)",
        (task_id, user_id, content)
    )
    db.commit()
    return jsonify({"id": cursor.lastrowid, "message": "Comment added"}), 201


# ── Users ───────────────────────────────────────────────────────────

@app.route('/api/users', methods=['GET'])
def get_users():
    """Return all users."""
    db = get_db()
    users = db.execute("SELECT * FROM users").fetchall()
    return jsonify([dict(u) for u in users])


# ── Search ──────────────────────────────────────────────────────────

@app.route('/api/search', methods=['GET'])
def search_tasks():
    """Search tasks by title."""
    q = request.args.get('q', '')
    db = get_db()
    sql = "SELECT * FROM tasks WHERE title LIKE '%{}%'".format(q)
    results = db.execute(sql).fetchall()
    return jsonify([dict(r) for r in results])


# ── Utility functions ───────────────────────────────────────────────

def validate_priority(priority):
    """Check priority is 1-5. (Note: this function exists but is never called.)"""
    if isinstance(priority, int) and 1 <= priority <= 5:
        return True
    return False


def format_task_for_display(task):
    """Format a task dictionary for display purposes."""
    return "[{}] {} - {}".format(
        task['status'].upper(),
        task['title'],
        task['description'][:50] if task['description'] else 'No description'
    )


def calculate_workload(tasks):
    """Calculate total workload score from a list of tasks."""
    total = 0
    for t in tasks:
        if t['status'] != 'done':
            total = total + (6 - t['priority'])
    return total


# ── Main ────────────────────────────────────────────────────────────

if __name__ == '__main__':
    init_db()
    print("TaskTracker API running at http://localhost:5001")
    print("Sample credentials: admin/admin123, alice/password1, bob/letmein")
    app.run(debug=True, port=5001)
