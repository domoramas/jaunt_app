from django import forms
from django.forms import widgets, ModelForm
from . import models
from artist_profile.models import ArtistProfile
from users.models import CustomUser
from django.utils.translation import gettext_lazy as _
import datetime


VENUE_SIZE_CHOICES = [
  ( "50- 150", "SM (50- 150)"),
  ("151 - 500", "MD (151 - 500)"),
  ("500-1000", "LG (500-1000)")
]

REGION_CHOICES = [
  ("NorthWest", "NorthWest"),
  ("California", "California"),
  ("SouthWest", "SouthWest"),
  
  ]

class CreateTour(forms.Form):
  
  artist = forms.ModelChoiceField(queryset= ArtistProfile.objects.all())
    
  tour_name = forms.CharField(
    max_length= 200, 
    label= "Tour Name",
    )
  performers = forms.CharField(
    max_length= 200
    )
  guarantee = forms.IntegerField(
    label="Guarantee $"
    )
  door_split = forms.BooleanField(required= False)
  hotel_needed = forms.BooleanField(required= False)
  venue_size = forms.CharField(
    widget=forms.Select( 
    choices=VENUE_SIZE_CHOICES)
    )
     #  set start and end dates to todays date by default
  date_start = forms.DateField(widget= forms.SelectDateWidget, label= "Start Date", initial = datetime.date.today)
  date_end = forms.DateField(widget= widgets.SelectDateWidget, label= "End Date", initial = datetime.date.today)
  region = forms.MultipleChoiceField(
    widget=forms.CheckboxSelectMultiple,
    choices=REGION_CHOICES)


  def __init__(self, user, *args, **kwargs):
    super(CreateTour, self).__init__(*args, **kwargs)
    self.fields['artist'].queryset = ArtistProfile.objects.filter(user=user)


class CreateTourModelform(ModelForm):
   class Meta:
    model= models.Tour
    fields= ('artist','tour_name', 'performers', "guarantee", "door_split", "hotel_needed", 'venue_size', 'date_start', 'date_end', 'region', )
    labels = {
      'tour_name': _('Tour Name'),
      'guarantee': _('Guarantee $'),
      'date_start': _('Start Date'), 
      'date_end': _('End Date'),
    }
    widgets = {
      "venue_size" : forms.Select( 
        choices=VENUE_SIZE_CHOICES),
      "start_date" : widgets.SelectDateWidget,
      "end_date" : widgets.SelectDateWidget,
      "region" : forms.SelectMultiple(
        choices=REGION_CHOICES),
    }
    queryset = {
      'artist' : ArtistProfile.objects.all(),
    }

    def __init__(self, user, *args, **kwargs):
      super(CreateTour, self).__init__(*args, **kwargs)
      self.fields['artist'].queryset = ArtistProfile.objects.filter(user=user)



      # add image upload for tour flyers and press release