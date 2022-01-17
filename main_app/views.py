from dataclasses import field
from datetime import date
from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from django.views.generic import CreateView, UpdateView, DeleteView

# class Book:
#     def __init__(self, name, genre, description, date_published):
#         self.name = name
#         self.genre = genre
#         self.description = description
#         self.date_published = date_published
    
# books = [
#     Book('The Forever War', 'Science Fiction', 'Story of a soldier who returns home from war. Decades pass between each visit, but it feels like months for him due to time dialation', 1974),
#     Book('Game of Thrones', 'Fantasy', 'People fight over things', 1996),
#     Book('The Last Book in the Universe', 'Science Fiction', 'A young boy searches for a future in a dystopic world', 2002),
# ]

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
    return render(request, 'books/detail.html', { 'book': book })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['genre', 'description', 'date_published']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books/'