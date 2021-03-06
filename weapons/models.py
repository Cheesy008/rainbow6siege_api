from django.db import models

from operators.models import (
    Operator,
    Organization,
)


class AbstractWeapon(models.Model):

    class WeaponTypes(models.TextChoices):
        ASSAULT_RIFLE = 'Assault Rifle'
        MARKSMAN_RIFLE = 'Marksman Rifle'
        SHOTGUN = 'Shotgun'
        MACHINE_PISTOL = 'Machine Pistol'
        GADGET = 'Gadget'
        SUBMACHINE_GUN = 'Submachine gun'
        HANDGUN = 'Handgun'

    name = models.CharField(
        max_length=150,
        verbose_name='Name',
    )
    type = models.CharField(
        max_length=100,
        choices=WeaponTypes.choices,
        default=WeaponTypes.ASSAULT_RIFLE,
        verbose_name='Type',
    )
    users = models.ManyToManyField(
        Operator,
        verbose_name='Operators',
    )
    affiliation = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
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
    users = models.ManyToManyField(
        Operator,
        verbose_name='Users',
        related_name='weapons',
    )
    standard_damage = models.CharField(
        max_length=200,
        verbose_name='Standard damage',
        null=True,
    )
    suppressed_damage = models.CharField(
        max_length=200,
        verbose_name='Standard damage',
        null=True,
    )
    rate_of_fire = models.CharField(
        max_length=200,
        verbose_name='Rate of fire',
        null=True,
    )
    magazine_size = models.CharField(
        max_length=100,
        verbose_name='Magazine size',
        null=True,
    )
    ammunition_type = models.CharField(
        max_length=100,
        verbose_name='Ammunition type',
        null=True,
    )
    sights = models.ManyToManyField(
        'Attachments',
        related_name='sights',
        verbose_name='Sights',
    )
    barrels = models.ManyToManyField(
        'Attachments',
        related_name='barrels',
        verbose_name='Barrels',
    )
    grips = models.ManyToManyField(
        'Attachments',
        related_name='grips',
        verbose_name='Grips',
    )
    under_barrels = models.ManyToManyField(
        'Attachments',
        related_name='under_barrels',
        verbose_name='Under Barrels',
    )

    def __str__(self):
        return self.name

    class Meta(AbstractWeapon.Meta):
        verbose_name = 'Weapon'
        verbose_name_plural = 'Weapons'


class Gadget(AbstractWeapon):
    users = models.ManyToManyField(
        Operator,
        verbose_name='Users',
        related_name='gadgets',
    )

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
        max_length=7,
        choices=AttachmentsType.choices,
        default=AttachmentsType.SIGHT,
    )
    name = models.CharField(
        max_length=150,
    )

    def __str__(self):
        return f'{self.get_type_display()} - {self.name}'

    class Meta:
        verbose_name = 'Attachment'
        verbose_name_plural = 'Attachments'


class Loadout(models.Model):
    operator = models.OneToOneField(
        Operator,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Operator',
    )
    primary_weapons = models.ManyToManyField(
        Weapon,
        related_name='loadout_as_primary',
        verbose_name='Primary weapons',
    )
    secondary_weapons = models.ManyToManyField(
        Weapon,
        related_name='loadout_as_secondary',
        verbose_name='Secondary weapons',
    )
    gadgets = models.ManyToManyField(
        Weapon,
        related_name='loadout_as_gadgets',
        verbose_name='Gadgets',
    )

    def __str__(self):
        return f'{self.operator.name}(loadout)'

    class Meta:
        verbose_name = 'Loadout'
        verbose_name_plural = 'Loadouts'
