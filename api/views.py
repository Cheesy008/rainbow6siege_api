from rest_framework.viewsets import ReadOnlyModelViewSet

from operators.models import (
    Operator,
)
from .serializers import (
    OperatorSerializer,
)


class OperatorsViewSet(ReadOnlyModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
