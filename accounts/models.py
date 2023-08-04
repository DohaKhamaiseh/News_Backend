from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    location = models.CharField(max_length=256,default="jo")
    # add additional fields in here

    def __str__(self):
        return self.username
