from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    bookname = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    picbook = models.ImageField(upload_to='book_image',blank=True, null=True)
    info = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    related = models.ManyToManyField('self', related_name='id', blank=True)

    def __str__(self):
        return self.bookname



