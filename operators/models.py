from django.db import models
import datetime

from weapons.models import Weapon


class Operator(models.Model):

    class ArmorRating(models.TextChoices):
        LIGHT = '1', 'Light'
        MEDIUM = '2', 'Medium'
        HEAVY = '3', 'Heavy'

    class SpeedRating(models.TextChoices):
        SLOW = '1', 'Slow'
        NORMAL = '2', 'Normal'
        FAST = '3', 'Fast'

    name = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Name',
    )
    real_name = models.CharField(
        max_length=200,
        null=True,
        blank=True,
        verbose_name='Real name',
    )
    biography = models.TextField(
        null=True,
        blank=True,
        verbose_name='Biography',
    )
    psychological_profile = models.TextField(
        null=True,
        blank=True,
        verbose_name='Psychological profile',
    )
    organizations = models.ManyToManyField(
        'Organization',
        on_delete=models.PROTECT,
        related_name='operators',
        verbose_name='Organizations',
    )
    is_attacker = models.BooleanField(
        default=False,
        verbose_name='Is attacker',
    )
    is_defender = models.BooleanField(
        default=False,
        verbose_name='Is attacker',
    )
    birthplace = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name='Birthplace',
    )
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Date of birth',
        default=datetime.date.today(),
    )
    height = models.FloatField(
        null=True,
        blank=True,
        default=0,
        verbose_name='Height',
    )
    weight = models.PositiveSmallIntegerField(
        null=True,
        blank=True,
        default=0,
        verbose_name='Weight',
    )
    armor_rating = models.CharField(
        null=True,
        blank=True,
        max_length=1,
        choices=ArmorRating.choices,
        default=ArmorRating.LIGHT,
    )
    speed_rating = models.CharField(
        null=True,
        blank=True,
        max_length=1,
        choices=SpeedRating.choices,
        default=SpeedRating.SLOW,
    )
    unique_ability = models.CharField(
        max_length=200,
        verbose_name='Unique ability',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Operator'
        verbose_name_plural = 'Operators'


class Organization(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Name',
    )
    description = models.TextField(
        verbose_name='Description',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'


class Loadout(models.Model):
    operator = models.OneToOneField(
        Operator,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name='Operator',
    )
    description = models.TextField(
        verbose_name='Description',
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



