from django.db import models


class Brewery(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)


class Style(models.Model):
    name = models.CharField(max_length=255)


class Beer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    style = models.ForeignKey(Style, on_delete=models.PROTECT)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)


class Venue(models.Model):
    TYPE_BAR = 'bar'
    TYPE_BREWERY = 'brew'
    TYPE_FOOD_TRUCK = 'truck'
    TYPE_CHOICES = (
        (TYPE_BAR, 'Bar'),
        (TYPE_BREWERY, 'Brewery'),
        (TYPE_FOOD_TRUCK, 'Food Truck'),
    )

    name = models.CharField(max_length=255)
    description = models.TextField()
    venue_type = models.CharField(max_length=5, choices=TYPE_CHOICES)
    beers = models.ManyToManyField(Beer, related_name='venues')
