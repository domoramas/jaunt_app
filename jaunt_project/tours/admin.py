from django.contrib import admin
from .models import Tour, Venue, City, Region

# Register your models here.
admin.site.register(Tour)
admin.site.register(Venue)
admin.site.register(City)
admin.site.register(Region)