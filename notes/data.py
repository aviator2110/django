from copy import deepcopy
from datetime import datetime
from typing import Any

_NOTES: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Django introduction",
        "content": "Lorem ipsum dolor",
        "tags": ["python", "django", "web", "backend"],
        "category": "backend",
        "created_at": datetime(2026, 8, 14),
    },
    {
        "id": 2,
        "title": "Django models",
        "content": "Working with models and database relationships",
        "tags": ["django", "database", "orm"],
        "category": "backend",
        "created_at": datetime(2026, 7, 3),
    },
    {
        "id": 3,
        "title": "Django REST Framework",
        "content": "Building APIs with serializers and viewsets",
        "tags": ["drf", "django", "api", "rest", "backend"],
        "category": "backend",
        "created_at": datetime(2026, 9, 8),
    },
    {
        "id": 4,
        "title": "Python type hints",
        "content": "Using type annotations to make code easier to understand",
        "tags": ["python", "typing", "mypy"],
        "category": "programming",
        "created_at": datetime(2026, 6, 21),
    },
    {
        "id": 5,
        "title": "PostgreSQL basics",
        "content": "Creating tables, indexes, and writing SQL queries",
        "tags": ["postgresql", "sql", "database", "indexes"],
        "category": "database",
        "created_at": datetime(2026, 5, 17),
    },
    {
        "id": 6,
        "title": "Git commands",
        "content": "Useful commands for everyday Git workflow",
        "tags": ["git", "github", "version-control", "cli", "workflow"],
        "category": "tools",
        "created_at": datetime(2026, 8, 29),
    },
    {
        "id": 7,
        "title": "Docker introduction",
        "content": "Running applications inside isolated containers",
        "tags": ["docker", "containers", "devops"],
        "category": "devops",
        "created_at": datetime(2026, 4, 11),
    },
    {
        "id": 8,
        "title": "REST API principles",
        "content": "Understanding resources, HTTP methods, and status codes",
        "tags": ["rest", "api", "http", "backend", "web"],
        "category": "backend",
        "created_at": datetime(2026, 9, 2),
    },
    {
        "id": 9,
        "title": "Clean code",
        "content": "Writing readable, maintainable, and reusable code",
        "tags": ["clean-code", "python", "refactoring", "best-practices"],
        "category": "programming",
        "created_at": datetime(2026, 3, 26),
    },
    {
        "id": 10,
        "title": "Unit testing in Python",
        "content": "Testing application logic with pytest",
        "tags": ["testing", "pytest", "python", "tdd", "quality"],
        "category": "programming",
        "created_at": datetime(2026, 7, 19),
    },
]

_next_id = 11

def list_notes() -> list[dict[str, Any]]:
    return deepcopy(_NOTES)


def get_note(note_id: int) -> dict[str, Any] | None:
    for note in _NOTES:
        if note["id"] == note_id:
            return deepcopy(note)
    return None


def create_note(
        *,
        title: str,
        content: str,
        tags: list[str],
        category: str,
        created_at: datetime,
) -> dict[str, Any]:
    global _next_id

    note = {
        "id": _next_id,
        "title": title,
        "content": content,
        "tags": tags,
        "category": category,
        "created_at": created_at,
    }

    _NOTES.append(note)
    _next_id += 1

    return note


def update_note(
    note_id: int,
    title: str,
    category: str,
    tags: list[str],
    content: str,
    created_at: datetime,
):
    note: dict[str, Any] = {}

    for n in _NOTES:
        if n["id"] == note_id:
            note = n

    note["title"] = title
    note["category"] = category
    note["tags"] = tags
    note["content"] = content
    note["created_at"] = created_at

    return note


def delete_note(note_id: int):
    global _NOTES

    _NOTES = [note for note in _NOTES if note["id"] != note_id]