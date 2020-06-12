from django_filters import rest_framework as filters

from operators.models import (
    Organization,
    Operator,
)


class OperatorsFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )
    organization = filters.CharFilter(
        field_name='organizations__name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Operator
        fields = ('name', 'organization')
