# in chatbot/models.py

from django.db import models

class Chat(models.Model):
    user_input = models.CharField(max_length=255)
    bot_response = models.TextField()
