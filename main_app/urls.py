from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('books/', views.books_index, name='index'),
    path('books/<int:book_id>/', views.books_detail, name='detail'),
    path('books/create/', views.BookCreate.as_view(), name='books_create'),
    path('books/<int:pk>/update', views.BookUpdate.as_view(), name='books_update'),
    path('books/<int:pk>/delete', views.BookDelete.as_view(), name='books_delete'),
    path('books/<int:book_id>/add_reprint/', views.add_reprint, name='add_reprint'),
    path('books/<int:book_id>/assoc_author/<int:author_id>/', views.assoc_author, name='assoc_author'),
    path('authors/', views.AuthorList.as_view(), name='authors_index'),
    path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='authors_detail'),
    path('authors/create/', views.AuthorCreate.as_view(), name='authors_create'),
    path('authors/<int:pk>/update/', views.AuthorUpdate.as_view(), name='authors_update'),
    path('authors/<int:pk>/delete/', views.AuthorDelete.as_view(), name='authors_delete'),
]
