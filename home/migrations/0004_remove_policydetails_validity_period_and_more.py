# Generated by Django 5.0.3 on 2024-05-20 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_policydetails_policy_end_date_policy_start_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='policydetails',
            name='validity_period',
        ),
        migrations.AddField(
            model_name='policydetails',
            name='validity_period_years',
            field=models.IntegerField(default=1),
        ),
    ]