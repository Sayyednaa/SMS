# in notes/views.py
from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render, redirect
from .models import Note
from django.http import HttpResponse
import os
from django.shortcuts import render
from .models import  Note
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)

@login_required
def home(request):
    # fetch all tasks and notes from the database
   
    notes = Note.objects.all()

    # pass tasks and notes to the template context
    context = {
      
        'notes': notes
    }

    return render(request, 'notes/home.html', context)
@user_passes_test(lambda u: u.is_superuser)
@login_required
def note_upload(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        file = request.FILES['file']
        note = Note.objects.create(title=title, description=description, file=file)
        return redirect('/notes')
    return render(request, 'notes/note_form.html')
@user_passes_test(lambda u: u.is_superuser)
@login_required
def delete_note(request, note_id):
    # fetch the note object from the database
    note = get_object_or_404(Note, id=note_id)

    # delete the note object
    note.delete()

    # redirect to the view_notes URL
    return redirect('/notes')


@user_passes_test(lambda u: u.is_superuser)
@login_required
def view_notes(request,note_id):
    # fetch all notes from the database
    notes = get_object_or_404(Note, id=note_id)

    # pass notes to the template context
    context = {
        'notes': notes
    }

    return render(request, 'notes/view_notes.html', context)

