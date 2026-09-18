from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.utils.html import escape

from notes import data


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    body = f"""
    <h1>Welcome to Django! This is main page!</h1>
    <p>
        <a href="{escape(reverse('notes_list'))}">
        Go to notes list
        </a>
    </p>
    """
    return HttpResponse(body)


def about(request: HttpRequest) -> HttpResponse:
    body = f"""
    <h1>About Jango project</h1>
    <p>
        This is my first jango project!
    </p>
    """
    return HttpResponse(body)


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    items: list[str] = []
    for note in notes:
        items.append(f"""
            <li>{escape(note["title"])}</li>
        """)
    return HttpResponse(items)