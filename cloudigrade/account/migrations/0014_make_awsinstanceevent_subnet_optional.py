# Generated by Django 2.0.7 on 2018-07-31 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_update_machineimage_properties'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awsinstanceevent',
            name='subnet',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
