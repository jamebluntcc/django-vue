from django.urls import re_path
from backend import views

urlpatterns = [
    re_path(r'add$', views.add,),
    re_path(r'books$', views.books)
]