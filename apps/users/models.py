from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    
    class Meta:
        app_label = 'users'

    def __str__(self):
        return self.name
