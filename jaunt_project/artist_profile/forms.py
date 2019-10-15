from django import forms
from  .models import ArtistImage, ArtistProfile

# create custom form to create/edit artist profile
# create check box or drop down for genre field to make it easier to catagorize 
GENRE_CHOICES = [
  ( "hip-hop/rap", "Hip-Hop/Rap"),
  ("rock", "Rock"),
  ("country", "Country"),
  ('folk', 'Folk'),
  ('edm', 'EDM'),
  ('punk', 'Punk'),
  ('heavy metal', 'Heavy Metal'),
  ('alternative', 'Alternative'),
  ('reggae', 'Reggae')
]
# drop down for state choices
STATE_CHOICES = [
  ('Alabama', 'AL'),
  ('Alaska', 'AK'),
  ('Arizona', 'AZ'),
  ('Arkansas', 'AR'),
  ('California', 'CA'),
  ('Colorado', 'CO'),
  ('Connecticut', 'CT'),
  ('District of Columbia','DC'),
  ('Delaware','DE'),
  ('Florida','FL'),
  ('Georgia','GA'),
  ('Hawaii','HI'),
  ('Idaho','ID'),
  ('Illinois','IL'),
  ('Indiana','IN'),
  ('Iowa','IA'),
  ('Kansas','KS'),
  ('Kentucky','KY'),
  ('Louisiana','LA'),
  ('Maine','ME'),
  ('Maryland','MD'),
  ('Massachusetts','MA'),
  ('Michigan','MI'),
  ('Minnesota', 'MN'),
  ('Mississippi','MS'),
  ('Missouri','MO'),
  ('Montana','MT'),
  ('Nebraska','NE'),
  ('Nevada','NV'),
  ('New Hampshire','NH'),
  ('New Jersey','NJ'),
  ('New Mexico','NM'),
  ('New York','NY'),
  ('North Carolina','NC'),
  ('North Dakota','ND'),
  ('Ohio','OH'),
  ('Oklahoma','OK'),
  ('Oregon','OR'),
  ('Pennsylvania','PA'),
  ('Rhode Island','RI'),
  ('South Carolina','SC'),
  ('South Dakota','SD'),
  ('Tennessee','TN'),
  ('Texas','TX'),
  ('Utah','UT'),
  ('Vermont','VT'),
  ('Virginia','VA'),
  ('Washington','WA'),
  ('West Virginia','WV'),
  ('Wisconsin','WI'),
  ('Wyoming','WY'),
  ]
#
# class CreateArtist(forms.Form):
  
#   artist = forms.ModelChoiceField(queryset= ArtistProfile.objects.all())
    
#   tour_name = forms.CharField(
#     max_length= 200, 
#     label= "Tour Name",
#     )
#   performers = forms.CharField(
#     max_length= 200
#     )
#   guarantee = forms.IntegerField(
#     label="Guarantee $"
#     )
#   door_split = forms.BooleanField(required= False)
#   hotel_needed = forms.BooleanField(required= False)
#   venue_size = forms.CharField(
#     widget=forms.Select( 
#     choices=VENUE_SIZE_CHOICES)
#     )
#      #  set start and end dates to todays date by default
#   date_start = forms.DateField(widget= forms.SelectDateWidget, label= "Start Date", initial = datetime.date.today)
#   date_end = forms.DateField(widget= widgets.SelectDateWidget, label= "End Date", initial = datetime.date.today)
#   region = forms.MultipleChoiceField(
#     widget=forms.CheckboxSelectMultiple,
#     choices=REGION_CHOICES)


#   def __init__(self, user, *args, **kwargs):
#     super(CreateTour, self).__init__(*args, **kwargs)
#     self.fields['artist'].queryset = ArtistProfile.objects.filter(user=user)


# class CreateArtistModelform(ModelForm):
#    class Meta:
#     model= models.ArtistProfile
#     fields= ('artist','tour_name', 'performers', "guarantee", "door_split", "hotel_needed", 'venue_size', 'date_start', 'date_end', 'region', )
#     labels = {
#       'tour_name': _('Tour Name'),
#       'guarantee': _('Guarantee $'),
#       'date_start': _('Start Date'), 
#       'date_end': _('End Date'),
#     }
#     widgets = {
#       "venue_size" : forms.Select( 
#         choices=VENUE_SIZE_CHOICES),
#       "start_date" : widgets.SelectDateWidget,
#       "end_date" : widgets.SelectDateWidget,
#       "region" : forms.SelectMultiple(
#         choices=REGION_CHOICES),
#     }
#     queryset = {
#       'artist' : ArtistProfile.objects.all(),
#     }

#     def __init__(self, user, *args, **kwargs):
#       super(CreateTour, self).__init__(*args, **kwargs)
#       self.fields['artist'].queryset = ArtistProfile.objects.filter(user=user)



class ImageForm(forms.ModelForm):
    
    class Meta:
      model = ArtistImage
      fields = ('image',)


# create check box field for genres 
# drop down list for state
