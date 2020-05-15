from django.db import models
import datetime


class Operator(models.Model):

    class ArmorRating(models.TextChoices):
        LIGHT = '1', 'Light'
        MEDIUM = '2', 'Medium'
        HEAVY = '3', 'Heavy'

    class SpeedRating(models.TextChoices):
        SLOW = '1', 'Slow'
        NORMAL = '2', 'Normal'
        FAST = '3', 'Fast'

    class Position(models.TextChoices):
        DEFENDER = 'DEF', 'Defender'
        ATTACKER = 'ATT', 'Attacker'

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
        related_name='operators',
        verbose_name='Organizations',
    )
    position = models.CharField(
        max_length=3,
        choices=Position.choices,
        default=Position.DEFENDER
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
        default=datetime.date.today,
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






