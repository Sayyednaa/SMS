# in dictionary/views.py

import requests
from django.shortcuts import render
import os
import openai
from chatbot.chatbot import generate_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)

@login_required
def dictionary(request):
    if request.method == 'POST':
        word = request.POST['word']
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')
        data = response.json()

        input=f"Translate this into Hindi and Urdu:\n {word}\n"
        aires=generate_response(input)
        return render(request, 'dictionary/dictionary.html', {'data': data,'response':response,'aires':aires})
  
    return render(request, 'dictionary/dictionary.html')
# from .models import Word

# def dictionary_home(request):
#     # fetch all words from the database
#     words = Word.objects.all()

#     # pass words to the template context
#     context = {
#         'words': words
#     }

#     return render(request, 'dictionary/dictionary_home.html', context)