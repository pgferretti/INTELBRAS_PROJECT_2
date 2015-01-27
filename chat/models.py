from django.db import models

class Chat(models.Model):
    name = models.CharField(max_length=100)
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)