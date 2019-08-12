from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from .forms import CreateTour, CreateTourModelform
from artist_profile.models import ArtistProfile, ArtistImage
from artist_profile.forms import ImageForm
from .models import Tour, Venue, City
import ast



# need to create python TPS to creat optimum route 
#look at RESTApi to use React front end
# create tour proposal and then compile list of cities to book
def tour_proposal(request): 
  if request.method == "POST":
    form = CreateTour(request.user, request.POST)
    if form.is_valid():
      artist = form.cleaned_data["artist"]
      tour_name = form.cleaned_data["tour_name"]
      performers = form.cleaned_data["performers"]
      guarantee = form.cleaned_data["guarantee"]
      door_split = form.cleaned_data["door_split"]
      venue_size = form.cleaned_data["venue_size"]
      date_start = form.cleaned_data["date_start"]
      date_end = form.cleaned_data["date_end"]
      region = form.cleaned_data["region"]
      tour = Tour(
        artist= artist,
        tour_name=tour_name, 
        performers =performers,
        guarantee = guarantee,
        door_split = door_split,
        venue_size = venue_size,
        date_start = date_start,
        date_end = date_end,
        region = region,
      )
      tour.save()
      cities = City.objects.order_by('priority')
      days = tour.date_end - tour.date_start
      days = (days.days) +1
      print(days)
      city_list = []
      while days >= len(city_list) and len(cities) > len(city_list):
        for city in cities:
          if city.priority == 1:
            if days > 0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
          elif city.priority == 2:
            if days >0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
          elif city.priority == 3:
            if days > 0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
      tour.city_list = city_list
      tour.save()
      form = CreateTour(request.user)
      return HttpResponseRedirect(reverse('tours:tours_detail', args=(tour.id,) ))
  elif request.method == "GET":
    form = CreateTour(request.user)
  return render(request, "tour_create.html", {'form': form} )

#  function view for making to update the form
def edit(request, pk):
  tour = get_object_or_404(Tour, pk=pk)
  if request.method == "POST":
    form = CreateTour(request.user, request.POST)
    if form.is_valid():
      tour.artist = form.cleaned_data["artist"]
      tour.tour_name = form.cleaned_data["tour_name"]
      tour.performers = form.cleaned_data["performers"]
      tour.guarantee = form.cleaned_data["guarantee"]
      tour.door_split = form.cleaned_data["door_split"]
      tour.venue_size = form.cleaned_data["venue_size"]
      tour.date_start = form.cleaned_data["date_start"]
      tour.date_end = form.cleaned_data["date_end"]
      tour.region = form.cleaned_data["region"]
      tour.save()
      cities = City.objects.order_by('priority')
      days = tour.date_end - tour.date_start 
      days = (days.days) + 1
      print(days)
      print(len(cities))
      city_list = []
      while days >= len(city_list) and len(cities) > len(city_list):
        for city in cities:
          if city.priority == 1:
            if days > 0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
                print(city_list)
          if city.priority == 2:
            if days >0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
                print(city_list)
          if city.priority == 3:
            if days > 0:
              if (city.city, city.state) not in city_list:
                city_list.append((city.city, city.state))
                days -= 1
                print(city_list)
      tour.city_list = city_list
      tour.save()
      return HttpResponseRedirect(reverse('tours:tours_detail', args=(tour.id,) ))
  elif request.method == "GET":
    form = CreateTour(request.user, 
    initial={
    "artist" : tour.artist, 
    "tour_name" : tour.tour_name, 
    "performers": tour.performers, 
    "guarantee": tour.guarantee,
    "door_split": tour.door_split,
    "venue_size" : tour.venue_size,
    "date_start" : tour.date_start,
    "date_end" : tour.date_end,
    "region" : tour.region,
     })
  return render(request, "tour_edit.html", {'form': form} )

class DeleteTour(LoginRequiredMixin, DeleteView):
  model = Tour
  template_name= "tour_delete.html"
  success_url = reverse_lazy('home')

class TourView(LoginRequiredMixin, DetailView):
  model = Tour
  template_name = "tours_detail.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    cities = ast.literal_eval(self.object.city_list)
    context["cities"] = [City.objects.get(city= city[0]) for city in cities]
    return context

# class CreateTour(LoginRequiredMixin, CreateView):
#   model = Tour
#   form_class = CreateTourModelform
#   template_name = "tour_create.html"

# class UpdateTour(LoginRequiredMixin, UpdateView):
#   model = Tour
#   form_class = CreateTourModelform
#   template_name = "tour_edit.html"
    
