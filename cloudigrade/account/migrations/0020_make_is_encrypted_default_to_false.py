# Generated by Django 2.1 on 2018-08-21 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_add_error_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineimage',
            name='is_encrypted',
            field=models.BooleanField(default=False),
        ),
    ]