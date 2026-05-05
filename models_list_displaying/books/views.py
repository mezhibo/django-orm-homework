from datetime import datetime

from django.shortcuts import render

from books.models import Book


def books_view(request, pub_date=None):
    template = 'books/books_list.html'

    books = Book.objects.all().order_by('pub_date')

    previous_date = None
    next_date = None

    if pub_date:
        current_date = datetime.strptime(pub_date, '%Y-%m-%d').date()

        books = books.filter(pub_date=current_date)

        previous_book = (
            Book.objects
            .filter(pub_date__lt=current_date)
            .order_by('-pub_date')
            .first()
        )

        next_book = (
            Book.objects
            .filter(pub_date__gt=current_date)
            .order_by('pub_date')
            .first()
        )

        if previous_book:
            previous_date = previous_book.pub_date

        if next_book:
            next_date = next_book.pub_date

    context = {
        'books': books,
        'previous_date': previous_date,
        'next_date': next_date,
    }

    return render(request, template, context)
