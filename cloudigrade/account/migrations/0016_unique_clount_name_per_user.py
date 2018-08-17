# Generated by Django 2.1 on 2018-08-14 14:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0015_machineimage_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('user', 'name')},
        ),
    ]