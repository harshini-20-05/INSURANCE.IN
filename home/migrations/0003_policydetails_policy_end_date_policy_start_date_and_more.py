# Generated by Django 5.0.3 on 2024-05-20 05:01

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_policy_claim_transaction'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyDetails',
            fields=[
                ('policy_no', models.IntegerField(primary_key=True, serialize=False)),
                ('policy_type', models.CharField(max_length=20)),
                ('validity_period', models.CharField(max_length=20)),
                ('payment_period', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'policy_details',
            },
        ),
        migrations.AddField(
            model_name='policy',
            name='end_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='policy',
            name='start_date',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='policy',
            name='policy_no',
            field=models.ForeignKey(db_column='policy_no', on_delete=django.db.models.deletion.CASCADE, to='home.policydetails'),
        ),
    ]