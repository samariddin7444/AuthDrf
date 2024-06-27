from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    class Meta:
        db_table = 'custom_user'

    def __str__(self):
        return self.username
