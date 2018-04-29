from django.forms import ModelForm,Textarea
from .models import Book,Category


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ('bookname', 'price', 'picbook', 'info', 'category')

        # widgets = {
        #     'info': Textarea(attrs={'cols': 30, 'rows': 5}),
        # }
