from django.views.generic import DetailView, ListView

from . import models


class BeerDetail(DetailView):
    model = models.Beer


class BeerList(ListView):
    model = models.Beer


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
    model = models.Venue
