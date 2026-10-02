from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.middleware.csrf import get_token
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import escape
from notes.models import Note, Category, Tag
from notes import data
from notes.forms import ContactForm, NoteForm


def index(request: HttpRequest) -> HttpResponse:

    return render(request, 'notes/home.html')


def about(request: HttpRequest) -> HttpResponse:

    return render(request, 'notes/about.html')


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.select_related('author', 'category').prefetch_related('tags').order_by('-created_at')

    return render(request, 'notes/notes_list.html', {'notes': notes})


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(
        Note.objects.select_related('author', 'category').prefetch_related('tags'),
        pk=note_id
    )

    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, 'Note created successfully')
            return redirect('notes:note_detail', note_id=note.pk)
    else:
        form = NoteForm()
    return render(request, 'notes/note_create.html', {'form': form})


def note_edit(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            tags = form.cleaned_data['tags'].split(' ')
            data.update_note(
                note_id=note_id,
                title=title,
                content=content,
                category=category,
                tags=tags
            )

            return redirect('notes_list')
    else:
        form = NoteForm(initial=note)
    return render(request, 'notes/note_create.html', {'form': form})


def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if request.method == 'POST':
        data.delete_note(note_id)
        return render(request, 'notes/note_delete.html', {'deleted': True, 'note': note})

    return render(request, 'notes/note_delete.html', {'note': note})

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            request.session['feedback_data'] = form.cleaned_data
            return redirect('feedback_confirm')
    else:
        feedback_data = request.session.get('feedback_data')
        form = ContactForm(initial=feedback_data) if feedback_data else ContactForm()

    return render(request, 'notes/contact.html', {'form': form})


def feedback_confirm(request: HttpRequest, form: ContactForm | None = None) -> HttpResponse:
    feedback_data = request.session.get('feedback_data')
    if not feedback_data:
        return redirect('notes_feedback')

    if request.method == 'POST':
        if request.POST.get('action') == 'back':
            return redirect('notes_feedback')

        request.session.pop('feedback_data', None)
        return redirect('feedback_success')

    return render(request, 'notes/feedback_confirm.html', {
        'feedback': feedback_data,
        'data': feedback_data,
    })


def feedback_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'notes/feedback_success.html')