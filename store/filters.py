import django_filters
from .models import *
from django_filters import DateFilter, CharFilter

class ProductFilter(django_filters.FilterSet):
	title = CharFilter(field_name='title', lookup_expr='icontains')
	price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
	price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
	
   
	class Meta:
		model = Product
		fields = ['title', 'brends', 'colors']
		