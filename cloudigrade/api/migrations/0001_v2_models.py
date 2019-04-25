# Generated by Django 2.1.5 on 2019-05-01 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AwsCloudAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('aws_account_id', models.DecimalField(db_index=True, decimal_places=0, max_digits=12)),
                ('account_arn', models.CharField(max_length=256, unique=True)),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwsEC2InstanceDefinitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('instance_type', models.CharField(db_index=True, max_length=256, unique=True)),
                ('memory', models.DecimalField(decimal_places=2, default=0, max_digits=16)),
                ('vcpu', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwsInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ec2_instance_id', models.CharField(db_index=True, max_length=256, unique=True)),
                ('region', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwsInstanceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subnet', models.CharField(blank=True, max_length=256, null=True)),
                ('instance_type', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwsMachineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ec2_ami_id', models.CharField(db_index=True, max_length=256, unique=True)),
                ('platform', models.CharField(choices=[('none', 'None'), ('windows', 'Windows')], default='none', max_length=7, null=True)),
                ('owner_aws_account_id', models.DecimalField(decimal_places=0, max_digits=12, null=True)),
                ('region', models.CharField(blank=True, max_length=256, null=True)),
                ('aws_marketplace_image', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CloudAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('name', models.CharField(db_index=True, max_length=256)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('cloud_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.CloudAccount')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstanceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('event_type', models.CharField(choices=[('power_on', 'power_on'), ('power_off', 'power_off'), ('attribute_change', 'attribute_change')], max_length=32)),
                ('occurred_at', models.DateTimeField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Instance')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MachineImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('object_id', models.PositiveIntegerField()),
                ('inspection_json', models.TextField(blank=True, null=True)),
                ('is_encrypted', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('pending', 'Pending Inspection'), ('preparing', 'Preparing for Inspection'), ('inspecting', 'Being Inspected'), ('inspected', 'Inspected'), ('error', 'Error'), ('unavailable', 'Unavailable for Inspection')], default='pending', max_length=32)),
                ('rhel_challenged', models.BooleanField(default=False)),
                ('openshift_detected', models.BooleanField(default=False)),
                ('openshift_challenged', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Run',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('instance_type', models.CharField(blank=True, max_length=64, null=True)),
                ('memory', models.FloatField(blank=True, default=0, null=True)),
                ('vcpu', models.IntegerField(blank=True, default=0, null=True)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Instance')),
                ('machineimage', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MachineImage')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AwsMachineImageCopy',
            fields=[
                ('awsmachineimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.AwsMachineImage')),
                ('reference_awsmachineimage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.AwsMachineImage')),
            ],
            options={
                'ordering': ('created_at',),
                'abstract': False,
            },
            bases=('api.awsmachineimage',),
        ),
        migrations.AddField(
            model_name='instance',
            name='machine_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.MachineImage'),
        ),
        migrations.AlterUniqueTogether(
            name='cloudaccount',
            unique_together={('user', 'name')},
        ),
    ]
