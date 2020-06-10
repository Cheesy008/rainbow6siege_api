from rest_framework.viewsets import ReadOnlyModelViewSet

from operators.models import (
    Operator,
    Organization,
)
from .serializers import (
    OperatorListSerializer,
    OperatorDetailSerializer,
    OrganizationListSerializer,
)
from .pagination import PaginationSettings


class OperatorsViewSet(ReadOnlyModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorListSerializer
    pagination_class = PaginationSettings

    def get_serializer_class(self):
        if self.action == 'list':
            return OperatorListSerializer
        elif self.action == 'retrieve':
            return OperatorDetailSerializer
        return super().get_serializer_class()


class OrganizationViewSet(ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationListSerializer

