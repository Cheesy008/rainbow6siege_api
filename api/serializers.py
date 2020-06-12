from rest_framework import serializers

from operators.models import (
    Operator,
    Organization,
)
from weapons.models import (
    Loadout, Weapon
)


class LoadoutListSerializer(serializers.ModelSerializer):
    primary_weapons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    secondary_weapons = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    gadgets = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Loadout
        fields = (
            'primary_weapons',
            'secondary_weapons',
            'gadgets',
        )


class OrganizationListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='organization-detail', read_only=True)

    class Meta:
        model = Organization
        fields = '__all__'


class OperatorListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='operator-detail', read_only=True)
    organizations = OrganizationListSerializer(many=True, read_only=True)

    class Meta:
        model = Operator
        fields = (
            'id',
            'url',
            'name',
            'position',
            'armor_rating',
            'speed_rating',
            'organizations',
        )
        read_only_fields = ('__all__',)


class OperatorDetailSerializer(serializers.ModelSerializer):
    organizations = OrganizationListSerializer(many=True, read_only=True)
    loadout = LoadoutListSerializer(read_only=True)

    class Meta:
        model = Operator
        fields = '__all__'
        read_only_fields = ('__all__',)


class WeaponListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='weapon-detail', read_only=True)
    users = OperatorListSerializer(many=True, read_only=True)

    class Meta:
        model = Weapon
        fields = (
            'id',
            'url',
            'name',
            'users',
        )


class WeaponDetailSerializer(serializers.ModelSerializer):
    users = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    sights = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    barrels = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    grips = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )
    under_barrels = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Weapon
        fields = '__all__'


