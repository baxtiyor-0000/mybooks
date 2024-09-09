from django.urls import path
from .views import book_list
from .views import book_detail_1
from .views import book_detail_2
from .views import book_detail_3

urlpatterns = [
    path('', book_list, name='book_list'),
    path('book/1/', book_detail_1, name='book_detail_1'),
    path('book/2/', book_detail_2, name='book_detail_2'),
    path('book/3/', book_detail_3, name='book_detail_3'),
]