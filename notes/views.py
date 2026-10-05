from django.http import HttpResponseForbidden
from django.contrib import messages
from django.contrib.auth.decorators import login_required
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


@login_required
def notes_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.filter(author=request.user).order_by('-created_at')

    return render(request, 'notes/notes_list.html', {'notes': notes})


@login_required
def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(
        Note.objects.select_related('author', 'category').prefetch_related('tags'),
        pk=note_id
    )
    if note.author != request.user:
        return HttpResponseForbidden(
            "You can only see notes owned by yourself."
        )

    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
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


@login_required
def note_edit(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if note.author != request.user:
        return HttpResponseForbidden(
            "You can only edit notes owned by yourself."
        )
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note updated successfully')
            return redirect('notes:note_detail', note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_create.html', {'form': form})


@login_required
def note_delete(request: HttpRequest, note_id: int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if note.author != request.user:
        return HttpResponseForbidden(
            "You can only delete notes owned by yourself."
        )
    if request.method == 'POST':
        note.delete()
        messages.success(request, 'Note deleted successfully')
        return redirect('notes:notes_list')
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