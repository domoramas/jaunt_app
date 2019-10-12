from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
  first_name = models.CharField(max_length= 30)
  last_name = models.CharField(max_length = 30)
  email  = models.EmailField()
  city = models.CharField(max_length = 12, null = True, blank=True )
  state = models.CharField( max_length = 2, null = True, blank=True )


  def __str__(self):
    return self.username


    # add title options for user - (artist, promoter, agent each with its own permission and views)
    # add first and last name 