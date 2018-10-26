# Generated by Django 2.1.1 on 2018-09-28 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_instanceevent_nullable_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='AwsEC2InstanceDefinitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instance_type', models.CharField(db_index=True, max_length=256, unique=True)),
                ('memory', models.FloatField(default=0)),
                ('vcpu', models.IntegerField(default=0)),
            ],
        ),
    ]