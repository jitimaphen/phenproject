from .models import Book,Category
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class BookSerializer(serializers.HyperlinkedModelSerializer):
    related = serializers.SlugRelatedField(many=True, read_only=True, slug_field='bookname')

    class Meta:
        model = Book
        fields = ('bookname', 'price', 'picbook', 'info', 'category_id', 'related')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
