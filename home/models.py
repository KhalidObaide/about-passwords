from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=99999)
    password = models.CharField(max_length=99999)

    def __str__(self):
        return self.username
