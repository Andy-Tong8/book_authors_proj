from django.shortcuts import render, redirect
from .models import *

def books(request):
    context = {
        'books' : Book.objects.all(),
    }
    return render(request, 'books.html', context)

def authors(request):
    context = {
        'authors' : Author.objects.all(),
    }
    return render(request, 'authors.html', context)

def book_info(request,number):
    book = Book.objects.get(id=number)
    context = {
        'book' : book,
        'authors' : book.authors.all(),
        'add_authors' : Author.objects.exclude(books=Book.objects.get(id=number))
        #Author.objects.all().difference(book.authors.all())
    }
    return render(request, 'book_info.html', context)

def author_info(request,number):
    author = Author.objects.get(id=number)
    context = {
        'author' : author,
        'books' : author.books.all(),
        'add_books' : Book.objects.exclude(authors=Author.objects.get(id=number))
        #Book.objects.all().difference(author.books.all())
    } 
    return render(request, 'author_info.html', context)

def add_book(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def add_book_author(request, number):
    Book.objects.get(id=number).authors.add(Author.objects.get(id=request.POST['auth']))
    return redirect('/books/'+str(number))

def add_author(request):
    Author.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], notes=request.POST['notes'])
    return redirect('/authors')

def add_author_book(request, number):
    book = Book.objects.get(id=int(request.POST['book-id']))
    Author.objects.get(id=number).books.add(book)
    return redirect('/authors/'+str(number))










