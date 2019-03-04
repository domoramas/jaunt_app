from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from artist_profile.models import ArtistProfile, ArtistImage
from users.models import CustomUser

class DashboardView(generic.ListView):
  model = ArtistProfile
  template_name = "home.html"
  # context_object_name = 'artist_list'

  def get_queryset(self):
    return ArtistProfile.objects.filter(user__username= self.request.user)

  # def get_queryset(self):
  #   my_query =ArtistProfile.objects.filter(user__username= self.request.user)
  #   for artist in my_query:
  #     if artist.profile_pic:
  #       artist["profile_img"] = ArtistImage.objects.get(pk= artist.profile_pic)
  #   return my_query

  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   for artist in context['artistprofile_list']: 
  #     if artist.profile_pic:
  #       artist['profile_img'] = ArtistImage.objects.get(pk= artist.profile_pic)

  #   print(context)
  #   return context
