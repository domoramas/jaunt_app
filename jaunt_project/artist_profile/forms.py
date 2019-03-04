from django import forms
from  .models import ArtistImage

class ImageForm(forms.ModelForm):
    
    class Meta:
      model = ArtistImage
      fields = ('image',)


