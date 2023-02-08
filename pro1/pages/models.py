from django.db import models

# Create your models here.
class UserData(models.Model):
    username = models.CharField(max_length=10)
    password = models.CharField(max_length=10)
    email = models.EmailField()
    def __str__(self):
        return self.username