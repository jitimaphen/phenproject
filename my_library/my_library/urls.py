
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from book_management import viewsapi, views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'users', viewsapi.UserViewSet)
router.register(r'groups', viewsapi.GroupViewSet)
router.register(r'book', viewsapi.BookViewSet)
router.register(r'category', viewsapi.CategoryViewSet)


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'index', views.index),
    path(r'manage/', views.manage),
    path('detail/<int:cat>/', views.detail, name='detail'),
    path('<int:cat>/', views.detail, name='detail'),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))

    # path('articles/<int:year>/', views.year_archive, name='news-year-archive'),
    # url(r'^blogadmin', include('book_management.urls'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
