from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='items/')
    condition = models.CharField(max_length=50, choices=[
        ('novo', 'Novo'),
        ('usado', 'Usado'),
        ('bom', 'Em bom estado')
    ])
    owner = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name