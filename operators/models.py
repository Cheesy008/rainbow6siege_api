from django.db import models
from django.urls import reverse


class Operator(models.Model):

    class ArmorRating(models.TextChoices):
        LIGHT = 'Light'
        MEDIUM = 'Medium'
        HEAVY = 'Heavy'

    class SpeedRating(models.TextChoices):
        SLOW = 'Slow'
        NORMAL = 'Normal'
        FAST = 'Fast'

    class Position(models.TextChoices):
        DEFENDER = 'Defender'
        ATTACKER = 'Attacker'
        BOTH = 'Both'

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
        default='Unknown',
        verbose_name='Real name',
    )
    organizations = models.ManyToManyField(
        'Organization',
        related_name='operators',
        verbose_name='Organizations',
    )
    position = models.CharField(
        max_length=10,
        choices=Position.choices,
        default=Position.BOTH
    )
    birthplace = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name='Birthplace',
    )
    date_of_birth = models.CharField(
        null=True,
        blank=True,
        max_length=200,
        verbose_name='Date of birth',
    )
    age = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Age',
    )
    height = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name='Height',
    )
    weight = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name='Weight',
    )
    armor_rating = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=ArmorRating.choices,
        default=ArmorRating.MEDIUM,
    )
    speed_rating = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=SpeedRating.choices,
        default=SpeedRating.NORMAL,
    )
    unique_ability = models.CharField(
        max_length=200,
        default='Missing',
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

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Organization'
        verbose_name_plural = 'Organizations'






