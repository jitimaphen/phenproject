
from django.contrib import admin
from django.urls import path
from book_management import views
from django.conf.urls import url, include

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', views.index),
    path(r'manage/', include('book_management.urls')),
    # url(r'^blogadmin', include('book_management.urls'))

]
