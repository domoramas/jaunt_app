from django.urls import path
from . import views

app_name="artist_profile"
urlpatterns = [
    path('new/', views.create_artist, name='artist_create'),
    path('<int:pk>/', views.ArtistView.as_view(), name = 'artist_detail'),
    path('<int:pk>/edit/', views.EditArtistView.as_view(), name='artist_edit'),
    path('<int:pk>/delete/', views.DeleteArtistView.as_view(), name="artist_delete"),
    path('<int:pk>/upload/', views.ImageUploadView.as_view(), name="upload"),
    path('<int:pk>/image_choice/', views.ImageChoice.as_view(), name="image_choice"),
    path('<int:pk>/selectpic/', views.selectpic, name="selectpic"),
]