from django.contrib import admin
from django.urls import path

from books.views import books_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', books_view, name='index'),
    path('books/', books_view, name='books'),
    path('books/<str:pub_date>/', books_view, name='books_by_date'),
]
