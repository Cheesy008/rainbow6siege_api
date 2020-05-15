from django.db import models

from operators.models import (
    Operator,
    Organization,
)


class AbstractWeapon(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name='Name',
    )
    type = models.ForeignKey(
        'Type',
        on_delete=models.PROTECT,
        related_name='weapons',
        verbose_name='Type',
    )
    users = models.ManyToManyField(
        Operator,
        null=True,
        blank=True,
        related_name='weapons',
        verbose_name='Operators',
    )
    max_ammunition = models.CharField(
        max_length=200,
        default='1',
        verbose_name='Maximum ammunition',
    )
    affiliation = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name='weapons',
        verbose_name='Affiliation',
    )
    mobility = models.PositiveSmallIntegerField(
        default=0,
        null=True,
        blank=True,
        verbose_name='Mobility',
    )

    class Meta:
        abstract = True


class Weapon(AbstractWeapon):
    fire_modes = models.TextField(
        verbose_name='Fire modes',
    )
    standard_damage = models.CharField(
        max_length=200,
        verbose_name='Standard damage',
    )
    suppressed_damage = models.CharField(
        max_length=200,
        verbose_name='Standard damage',
    )
    rate_of_fire = models.CharField(
        max_length=200,
        verbose_name='Rate of fire',
    )
    magazine_size = models.CharField(
        max_length=100,
        verbose_name='Magazine size',
    )
    ammunition_type = models.CharField(
        max_length=100,
        verbose_name='Ammunition type',
    )
    sights = models.ManyToManyField(
        'Sight',
        related_name='weapons',
        verbose_name='Sights',
    )
    barrels = models.ManyToManyField(
        'Barrel',
        null=True,
        blank=True,
        related_name='weapons',
        verbose_name='Barrels',
    )
    grips = models.ManyToManyField(
        'Grip',
        null=True,
        blank=True,
        related_name='weapons',
        verbose_name='Grips',
    )
    under_barrels = models.ManyToManyField(
        'UnderBarrel',
        null=True,
        blank=True,
        related_name='weapons',
        verbose_name='Under Barrels',
    )

    def __str__(self):
        return self.name

    class Meta(AbstractWeapon.Meta):
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'


class Gadget(AbstractWeapon):

    class Meta(AbstractWeapon.Meta):
        verbose_name = 'Gadget'
        verbose_name_plural = 'Gadgets'


class Attachments(models.Model):
    class AttachmentsType(models.TextChoices):
        SIGHT = 'SI', 'Sight'
        BARREL = 'BAR', 'Barrel'
        GRIP = 'GR', 'Grip'
        UNDER_BARREL = 'UND_BAR', 'Under Barrel'

    type = models.CharField(
        max_length=2,
        choices=AttachmentsType.choices,
        default=AttachmentsType.SIGHT,
    )
    name = models.CharField(
        max_length=150,
    )
