from django_filters import FilterSet
from .models import Car




class CarFilter(FilterSet):
   class Meta:
       model = Car
       fields = {
           'brand': ['exact'],
           'year': ['gt', 'lt'],
           'price': ['gt', 'lt']
       }
