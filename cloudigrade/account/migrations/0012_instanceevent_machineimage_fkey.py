# Generated by Django 2.0.7 on 2018-07-06 19:49

from django.db import migrations, models
import django.db.models.deletion


def update_aws_event_images(apps, schema_editor):
    """Update existing events to reference corresponding images."""

    AwsInstanceEvent = apps.get_model('account', 'AwsInstanceEvent')
    AwsMachineImage = apps.get_model('account', 'AwsMachineImage')

    events = AwsInstanceEvent.objects.all()
    for event in events:
        image = AwsMachineImage.objects.get(ec2_ami_id=event.ec2_ami_id)
        event.machineimage = image
        event.save()


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_account_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='instanceevent',
            name='machineimage',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                null=True,
                to='account.MachineImage',
            ),
            preserve_default=False,
        ),
        migrations.RunPython(update_aws_event_images),
        migrations.RemoveField(
            model_name='awsinstanceevent',
            name='ec2_ami_id',
        ),
        migrations.AlterField(
            model_name='instanceevent',
            name='machineimage',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                null=False,
                to='account.MachineImage',
            ),
        ),

    ]