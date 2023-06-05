# in books/models.py

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='static/img/covers/', blank=True)
    pdf = models.FileField(upload_to='static/pdfs/')

    def __str__(self):
        return self.title
class PwLecs(models.Model):

    Subject = models.CharField(max_length=100,default=None)
    Chapter = models.CharField(max_length=100 ,default=None)
    LecN = models.CharField(max_length=100 ,default=None)
    Date = models.CharField(max_length=100 ,default=None)
    Watched = models.BooleanField(default=False)
    # Watched = models.CharField(max_length=100)
#
    def __str__(self):
        return self.Chapter
