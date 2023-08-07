# from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField

class CustomUser(AbstractUser):
    first_name = CharField(max_length="128", default="")
    last_name = CharField(max_length="128", default="")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"
