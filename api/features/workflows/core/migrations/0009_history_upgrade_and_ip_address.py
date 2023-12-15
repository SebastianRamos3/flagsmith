# Generated by Django 3.2.23 on 2023-12-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflows_core', '0008_remove_redundant_column'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='historicalchangerequest',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical change request', 'verbose_name_plural': 'historical change requests'},
        ),
        migrations.AlterModelOptions(
            name='historicalchangerequestapproval',
            options={'get_latest_by': ('history_date', 'history_id'), 'ordering': ('-history_date', '-history_id'), 'verbose_name': 'historical change request approval', 'verbose_name_plural': 'historical change request approvals'},
        ),
        migrations.AddField(
            model_name='historicalchangerequest',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='historicalchangerequestapproval',
            name='ip_address',
            field=models.GenericIPAddressField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='historicalchangerequest',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
        migrations.AlterField(
            model_name='historicalchangerequestapproval',
            name='history_date',
            field=models.DateTimeField(db_index=True),
        ),
    ]