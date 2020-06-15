from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.response import Response

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
from .tasks import send_email_task


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

    @action(detail=True, methods=['post', 'get'], serializer_class=OperatorDetailSerializer)
    def test_email(self, request, pk=None):
        user_email = request.user.email
        send_email_task.delay(user_email, 'Выполнено')
        return Response(status=status.HTTP_200_OK)


class WeaponViewSet(ReadOnlyModelViewSet):
    queryset = Weapon.objects.all()
    serializer_class = WeaponListSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return WeaponListSerializer
        elif self.action == 'retrieve':
            return WeaponDetailSerializer
        return super().get_serializer_class()
