# in books/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)


@login_required

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def book_upload(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_upload.html', {'form': form})



@user_passes_test(lambda u: u.is_superuser)
@login_required
def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'books/book_detail.html', {'book': book})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.delete()
    return redirect('/books')