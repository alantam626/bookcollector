from dataclasses import field
from datetime import date
from statistics import mode
from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from main_app.forms import ReprintForm
from .models import Book, Author


#Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all()
    return render(request, 'books/index.html', {'books': books })

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    authors_book_with_none = Author.objects.exclude(id__in = book.author.all().values_list('id'))
    reprint_form = ReprintForm()
    return render(request, 'books/detail.html', { 'book': book, 'reprint_form': reprint_form,
    'authors': authors_book_with_none 
    })

def add_reprint(request, book_id):
    form = ReprintForm(request.POST)
    if form.is_valid():
        new_reprint = form.save(commit=False)
        new_reprint.book_id = book_id
        new_reprint.save()
    return redirect('detail', book_id=book_id)

def  assoc_author(request, book_id, author_id):
    Book.objects.get(id=book_id).author.add(author_id)
    return redirect('detail', book_id=book_id)

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['genre', 'description', 'date_published']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'

class AuthorList(ListView):
    model = Author

class AuthorDetail(DetailView):
    model = Author

class AuthorCreate(CreateView):
    model = Author
    fields = '__all__'

class AuthorUpdate(UpdateView):
    model = Author
    fields = ['name']

class AuthorDelete(DeleteView):
    model = Author
    success_url = '/authors/'

