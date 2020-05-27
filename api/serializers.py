from rest_framework import serializers

from operators.models import (
    Operator,
    Organization,
)


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'

