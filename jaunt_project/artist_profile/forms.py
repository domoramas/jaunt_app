from django import forms
from  .models import ArtistImage

# create custom form to create/edit artist profile
# create check box or drop down for genre field to make it easier to catagorize 


class ImageForm(forms.ModelForm):
    
    class Meta:
      model = ArtistImage
      fields = ('image',)


# create check box field for genres 
# drop down list for state
