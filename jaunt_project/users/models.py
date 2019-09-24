from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length= 30)
  last_name = models.CharField(max_length = 30)


  def __str__(self):
    return self.username


    # add title options for user - (artist, promoter, agent each with its own permission and views)
    # add first and last name 