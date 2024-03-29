from django.db import models
from django.urls import reverse
from django.conf import settings

# added phone number field and country field.  not updating the db no migrations folder 

# move city, state, country and contact info to user set up
class ArtistProfile(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  artist_name = models.CharField(max_length= 30)
  city = models.CharField(max_length= 50,null=True, blank=True)
  state = models.CharField(max_length= 20,null=True, blank=True)
  genre = models.CharField(max_length= 30)
  description = models.TextField(max_length= 800, null=True, blank=True)
  website =models.URLField(max_length= 200, null=True, blank=True)
  profile_pic=models.ImageField(null=True, blank=True)
  profile_pic= models.IntegerField(null=True, blank=True)
  instagram= models.CharField(max_length=100, null=True, blank=True)
  twitter= models.CharField(max_length=100, null=True, blank=True)
  facebook= models.CharField(max_length=100, null=True, blank=True)
  bandcamp= models.CharField(max_length=100, null=True, blank=True)

  def __str__(self):
    return self.artist_name
  
  def get_absolute_url(self):
        return reverse('home')

class ArtistImage(models.Model):
  artist = models.ForeignKey(ArtistProfile, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='images/')
 
  # def get_absolute_url(self):
  #       return reverse('artist_profile:artist_detail', args=(artist.id))


  # find better way to store images for artist