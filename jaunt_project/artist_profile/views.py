from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from .forms import CreateArtist
from .models import ArtistProfile, ArtistImage
from .forms import ImageForm
from tours.models import Tour, Venue
from users.models import CustomUser
from django.conf import settings
# View of detailed Artist view
# select picture view breaks when no picture is selected

def create_artist(request): 

  if request.method == "POST":
    form = CreateArtist(request.user, request.POST)
    if form.is_valid():
      artist_name = form.cleaned_data["artist_name"]
      genre = form.cleaned_data["genre"]
      city = form.cleaned_data["city"]
      state = form.cleaned_data["state"]
      description = form.cleaned_data["description"]
      website = form.cleaned_data["website"]
      artist = ArtistProfile(
        artist_name= artist_name,
        genre =genre,
        city = city,
        state = state,
        description = description,
        # website = website
      )
      print(artist)
      artist.save()
      # form = CreateArtist(request.user)
      return HttpResponseRedirect(reverse('artist_profile:artist_detail', args=(artist.pk) ))
  elif request.method == "GET":    
    form = CreateArtist()
  return render(request, "artist_create.html", {'form': form} )


class ArtistView(LoginRequiredMixin, DetailView):
  model = ArtistProfile
  template_name = "artist.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['tours'] = Tour.objects.filter(artist__id =self.kwargs['pk'])
    if ArtistProfile.objects.get(pk= self.kwargs['pk']).profile_pic:
      profile_pic_id = ArtistProfile.objects.get(pk= self.kwargs['pk']).profile_pic
      context['profile_pic'] = ArtistImage.objects.get(pk= profile_pic_id)
    return context

# view to create artist view
# find way to integrate photo upload better

# class CreateArtistView(LoginRequiredMixin,CreateView):
#   model = ArtistProfile
#   template_name = 'artist_create.html'
#   form_class = CreateArtist
  

#   def form_valid(self, form):
#     form.instance.user = self.request.user
#     return super().form_valid(form)

class EditArtistView(LoginRequiredMixin, UpdateView):
  model = ArtistProfile
  template_name = 'artist_edit.html'
  fields = ['artist_name', 'genre', 'city', 'state','description','twitter','instagram', 'bandcamp']
class DeleteArtistView(LoginRequiredMixin, DeleteView):
  model = ArtistProfile
  template_name= "artist_delete.html"
  success_url = reverse_lazy('home')

# class to handle image uploads and add them to the db
class ImageUploadView(LoginRequiredMixin, CreateView):
  model = ArtistImage
  template_name = 'image_upload.html'
  fields = ['image']

  def get_success_url(self):
    artistid = self.kwargs['pk']
    return reverse_lazy("artist_profile:image_choice", kwargs={"pk": artistid})
  def form_valid(self, form):
    form.instance.artist = ArtistProfile.objects.get(pk = self.kwargs['pk'])
    return super().form_valid(form)
 
# View of detailed Artist Images view
class ImageChoice(LoginRequiredMixin, ListView):
  model = ArtistImage
  template_name = "image_choice.html"
  context_object_name = "image_list"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['artistpk'] = self.kwargs["pk"]
    return context

  def get_queryset(self):
    return ArtistImage.objects.filter(artist__id=self.kwargs["pk"])

# view for picking the image and saving the image id 
def selectpic(request, pk):
  artist = get_object_or_404(ArtistProfile, pk= pk)
  try:
    selected_image = artist.artistimage_set.get(pk = request.POST["pic"])
  except (KeyError, ArtistImage.DoesNotExist):
    return render(request, "artist.html", { 
      "artist": artist, 
      "error_message": "You didn't select a photo."
    })
  else:
    artist.profile_pic = request.POST["pic"]
    artist.save()
    return HttpResponseRedirect(reverse('artist_profile:artist_detail', args=(artist.id,)))


