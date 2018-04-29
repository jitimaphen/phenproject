from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from book_management.models import Category, Book
from .forms import BookForm


def index(request):

    context = {

            'book': Book.objects.all(),
            'cata': Category.objects.all(),
        }
    return render(request, 'book_management/index.html', context)


def manage(request):
    if request.method == "POST":
        form = BookForm(data=request.POST, files=request.FILES)
        # import ipdb; ipdb.set_trace()
        if form.is_valid():
            blog_item = form.save()
            blog_item.save()
    else:
        form = BookForm()
    return render(request, 'book_management/manage.html', {'form': form})

#
# def add_book(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             blog_item = form.save()
#             blog_item.save()
#     else:
#         form = BookForm()
#     return render(request, 'book_management/manage.html', {'form': form})


def detail(request, cat):

    context = {

            'book': Book.objects.filter(category=cat),
            'cata': Category.objects.all(),
        }
    return render(request, 'book_management/index.html', context)
