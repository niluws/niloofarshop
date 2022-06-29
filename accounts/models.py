from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
    email = models.CharField(max_length=100)
    active_code = models.CharField(max_length=100)

    def __str__(self):
        return self.email
