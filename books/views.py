from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from .models import Author, Book
from .forms import BookFormSet, BookForm

def create_book(request, pk):
    author = Author.objects.get(pk=pk)
    form = BookForm(request.POST or None)
    books = Book.objects.filter(author=author)

    if request.method == 'POST':
        if form.is_valid():
            book = form.save(commit=False)
            book.author = author
            book.save()
            return redirect("book-detail", pk=book.id)
        else:
            return redirect(request, "partials/book_form", {"form": form})
    context = {
        "form": form,
        "author": author,
        "books": books
    }

    return render(request, "create_book.html", context)

def create_book_form(request):
    context = {
        "form": BookForm()
    }
    return render(request, "partials/book_form.html", context)

def detail_book(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        "book": book,
    }
    return render(request, "partials/book_detail.html", context)

def update_book_form(request, pk):
    book = Book.objects.get(pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if request.method == 'POST':
        if form.is_valid():
            book = form.save()
            return redirect("book-detail", pk=book.id)
        else:
            return redirect(request, "partials/book_form", {"form": form, "book": book})

    context = {
        "form": form,
        "book": book
    }
    return render(request, "partials/book_form.html", context)


def delete_book(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()

    return HttpResponse("This book had been deleted")