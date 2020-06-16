# Generated by Django 3.0.4 on 2020-06-05 15:31

import logging

from django.db import migrations

logger = logging.getLogger(__name__)


def delete_concurrentusage_with_cloud_account_id(apps, schema_editor):
    """Delete verify_account_permissions PeriodicTasks that have no AwsCloudAccount."""
    ConcurrentUsage = apps.get_model("api", "ConcurrentUsage")

    concurrent_usages = ConcurrentUsage.objects.filter(cloud_account_id__isnull=False)
    logger.info(
        "Deleting %(number_concurrent)s ConcurrentUsages with cloud_account field set.",
        {"number_concurrent": concurrent_usages.count()},
    )
    concurrent_usages.delete()


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0023_machineimage_architecture"),
    ]

    operations = [
        migrations.RunPython(delete_concurrentusage_with_cloud_account_id),
    ]