from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ReadOnlyModelViewSet

from operators.models import (
    Operator,
    Organization,
)
from weapons.models import Weapon
from .serializers import (
    OperatorListSerializer,
    OperatorDetailSerializer,
    OrganizationListSerializer,
    WeaponListSerializer,
    WeaponDetailSerializer,
)
from .pagination import PaginationSettings
from .filters import OperatorsFilter


class OperatorsViewSet(ReadOnlyModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorListSerializer
    pagination_class = PaginationSettings
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OperatorsFilter

    def get_serializer_class(self):
        if self.action == 'list':
            return OperatorListSerializer
        elif self.action == 'retrieve':
            return OperatorDetailSerializer
        return super().get_serializer_class()


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer


class WeaponViewSet(ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return WeaponListSerializer
        elif self.action == 'retrieve':
            return WeaponDetailSerializer
        return super().get_serializer_class()
