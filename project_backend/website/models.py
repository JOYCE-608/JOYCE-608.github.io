from django.db import models

# Create your models here.

class Comment(models.Model):
    textfield = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    