# Generated by Django 3.0.7 on 2020-06-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weapons', '0002_auto_20200516_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gadget',
            name='type',
            field=models.CharField(choices=[('AS', 'Assault Rifle'), ('MR', 'Marksman Rifle'), ('SH', 'Shotgun'), ('MA', 'Machine Pistol'), ('GA', 'Gadget'), ('SU', 'Submachine gun'), ('HA', 'Handgun')], default='AS', max_length=2, verbose_name='Type'),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='type',
            field=models.CharField(choices=[('AS', 'Assault Rifle'), ('MR', 'Marksman Rifle'), ('SH', 'Shotgun'), ('MA', 'Machine Pistol'), ('GA', 'Gadget'), ('SU', 'Submachine gun'), ('HA', 'Handgun')], default='AS', max_length=2, verbose_name='Type'),
        ),
    ]