# Generated by Django 2.0.4 on 2018-04-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0002_auto_20180423_0540'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='related',
            field=models.ManyToManyField(related_name='_book_related_+', to='book_management.Book'),
        ),
    ]
