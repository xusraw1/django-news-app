from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('article/<int:pk>/detail/', article_detail, name='article_detail'),
    path('article/create/', article_create, name='article_create'),
    path('article/<int:pk>/update/', article_update, name='article_update'),
]
