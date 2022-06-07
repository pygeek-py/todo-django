import django_filters
from django_filters import CharFilter

from .models import item

class itemfilter(django_filters.FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")
    
    class Meta:
        model = item
        fields = '__all__'
        exclude = ['done', 'user']