from django.contrib import admin

from book_management.models import Category, Book

admin.site.register(Category)
admin.site.register(Book)