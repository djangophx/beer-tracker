from django.contrib import admin

from . import models


admin.site.register(models.Beer)
admin.site.register(models.Brewery)
admin.site.register(models.Style)
admin.site.register(models.Venue)
