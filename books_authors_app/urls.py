from django.urls import path
from . import views

urlpatterns = [
    path('',views.books),
    path('authors',views.authors),
    path('books/<int:number>',views.book_info),
    path('authors/<int:number>',views.author_info),
    path('add_book',views.add_book),
    path('add_book_author/<int:number>',views.add_book_author),
    path('add_author',views.add_author),
    path('add_author_book/<int:number>',views.add_author_book),
]