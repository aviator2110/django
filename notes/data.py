from copy import deepcopy
from typing import Any

_NOTES: list[dict[str, Any]] = [
    {
        "id": 1,
        "title": "Django introduction",
        "body": "Lorem ipsum dolor",
        "tag": "django",
        "category": "backend",
    },
    {
        "id": 2,
        "title": "Django models",
        "body": "Working with models and database relationships",
        "tag": "django",
        "category": "backend",
    },
    {
        "id": 3,
        "title": "Django REST Framework",
        "body": "Building APIs with serializers and viewsets",
        "tag": "drf",
        "category": "backend",
    },
    {
        "id": 4,
        "title": "Python type hints",
        "body": "Using type annotations to make code easier to understand",
        "tag": "python",
        "category": "programming",
    },
    {
        "id": 5,
        "title": "PostgreSQL basics",
        "body": "Creating tables, indexes, and writing SQL queries",
        "tag": "postgresql",
        "category": "database",
    },
    {
        "id": 6,
        "title": "Git commands",
        "body": "Useful commands for everyday Git workflow",
        "tag": "git",
        "category": "tools",
    },
    {
        "id": 7,
        "title": "Docker introduction",
        "body": "Running applications inside isolated containers",
        "tag": "docker",
        "category": "devops",
    },
    {
        "id": 8,
        "title": "REST API principles",
        "body": "Understanding resources, HTTP methods, and status codes",
        "tag": "rest",
        "category": "backend",
    },
    {
        "id": 9,
        "title": "Clean code",
        "body": "Writing readable, maintainable, and reusable code",
        "tag": "clean-code",
        "category": "programming",
    },
    {
        "id": 10,
        "title": "Unit testing in Python",
        "body": "Testing application logic with pytest",
        "tag": "testing",
        "category": "programming",
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
        body: str,
        tag: str,
        category: str,
) -> dict[str, Any]:
    global _next_id
    note = {
        "id": _next_id,
        "title": title,
        "body": body,
        "tag": tag,
        "category": category,
    }
    _NOTES.append(note)
    _next_id += 1
    return note


def update_note(
    note_id: int,
    title: str,
    category: str,
    tag: str,
    body: str,
):
    note: dict[str, Any] = {}

    for n in _NOTES:
        if n["id"] == note_id:
            note = n

    note["title"] = title
    note["category"] = category
    note["tag"] = tag
    note["body"] = body

    return note


def delete_note(note_id: int):
    global _NOTES

    _NOTES = [note for note in _NOTES if note["id"] != note_id]