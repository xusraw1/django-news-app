from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('article/<int:pk>/detail/', article_detail, name='article_detail'),
]
