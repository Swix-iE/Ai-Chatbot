from django.db import models

class Chat(models.Model):
    prompt = models.TextField
    response = models.TextField
    created = models.DateTimeField(auto_now_add=True)
    
