from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),
    path('upload/', views.book_upload, name='book_upload'),
    path('<int:pk>/', views.book_detail, name='book_detail'),
    path('delete/<int:pk>/', views.book_delete, name='book_delete'),
]