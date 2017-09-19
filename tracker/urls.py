from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^beers/$', views.BeerList.as_view(), name='beer-list'),
    url(r'^beers/(?P<pk>[0-9]+)/$', views.BeerDetail.as_view(), name='beer-detail'),
    url(r'^breweries/$', views.BreweryList.as_view(), name='brewery-list'),
    url(r'^breweries/(?P<pk>[0-9]+)/$', views.BreweryDetail.as_view(), name='brewery-detail'),
    url(r'^styles/$', views.StyleList.as_view(), name='style-list'),
    url(r'^styles/(?P<pk>[0-9]+)/$', views.StyleDetail.as_view(), name='style-detail'),
    url(r'^venues/$', views.VenueList.as_view(), name='venue-list'),
    url(r'^venues/(?P<pk>[0-9]+)/$', views.VenueDetail.as_view(), name='venue-detail'),
]
