from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'manage/', views.manage, name='add_book')
]