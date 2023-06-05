import openai
from django.http import JsonResponse
from django.shortcuts import render
from .chatbot import generate_response
from django.http import HttpResponse
# replace YOUR_API_KEY with your actual OpenAI API key
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(lambda u: u.is_superuser)

@login_required
def chatbot(request):
    if not request.user.is_authenticated:
        return HttpResponse("Login First")
    if request.method == 'POST':
        user_input = request.POST['user']
        response=generate_response(user_input)
        return render(request, 'chatbot/chatbot.html',{'response':response})
        # return bot response as JSON data
    return render(request, 'chatbot/chatbot.html')     

    
