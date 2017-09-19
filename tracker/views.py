from django.db.models import Count, Prefetch
from django.views.generic import DetailView, ListView

from . import models


class BeerDetail(DetailView):
    model = models.Beer


class BeerList(ListView):
    queryset = models.Beer.objects.select_related('brewery', 'style')


class BreweryDetail(DetailView):
    model = models.Brewery


class BreweryList(ListView):
    model = models.Brewery


class StyleDetail(DetailView):
    model = models.Style


class StyleList(ListView):
    model = models.Style


class VenueDetail(DetailView):
    model = models.Venue


class VenueList(ListView):
    queryset = models.Venue.objects.annotate(
        beer_count=Count('beers')
    ).prefetch_related(
        Prefetch(
            'beers',
            queryset=models.Beer.objects.select_related('brewery', 'style')
        )
    )
