from django import forms
from  .models import ArtistImage

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

class ImageForm(forms.ModelForm):
    
    class Meta:
      model = ArtistImage
      fields = ('image',)


# create check box field for genres 
# drop down list for state
