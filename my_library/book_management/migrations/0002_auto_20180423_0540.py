# Generated by Django 2.0.4 on 2018-04-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picbook',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
