# Generated by Django 3.0.4 on 2020-05-16 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operators', '0003_auto_20200516_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='operator',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
    ]