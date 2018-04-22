from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from book_management.models import Category, Book
from .forms import BookForm


def index(request):

    context = {
        'book': Book.objects.all(),
    }
    return render(request, 'book_management/index.html', context)


def manage(request):

    context = {
        'cat_num': len(Category.objects.all()),
        'book_num': len(Book.objects.all())
    }
    return render(request, 'book_management/manage.html', context)


# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             blog_item =form.save()
#             blog_item.save()
#     else:
#         form=BookForm()
#     return render(request, 'book_management/manage.html',{'form':form})