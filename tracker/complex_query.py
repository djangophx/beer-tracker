from dateutil.relativedelta import relativedelta

from django.db.models import Q
from django.utils import timezone


three_years = relativedelta(years=3)
five_years = relativedelta(years=5)
one_hundred_years = relativedelta(years=100)
one_month = relativedelta(months=1)
now = timezone.now()

stout = (
    (Q(style__name__icontains='stout') | Q(style__parent__name__icontains='stout')
    & Q(date_produced__range=(now - three_years, now - five_years))
)
ipa = Q(date_produced__gte=(now - one_month)) & Q(ibu__gte=90)
sour = Q(time_to_produce__gte=three_years)
belgian = (
    (Q(style__name__icontains='belgian') | Q(style__parent__name__icontains='belgian'))
    & Q(brewery__country='Belgium') & Q(brewery__established__lte=(now - one_hundred_years))
)

best_beers = (
    (stout | ipa | sour | belgian) & Q(avg_rating__gte=4.5)
    & ~Q(brewery__name__icontains='inbev')
)

beers = Beer.objects.filter(best_beers)

