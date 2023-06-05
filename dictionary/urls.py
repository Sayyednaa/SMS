from django.urls import path
from . import views



urlpatterns = [
    # path('', views.dictionary_home, name='dictionary_home'),
    path('', views.dictionary, name='dictionary_home'),
    # path('search_word/', views.search_word, name='search_word'),
]