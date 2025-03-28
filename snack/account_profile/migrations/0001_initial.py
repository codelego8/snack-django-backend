# Generated by Django 5.1.4 on 2025-03-05 08:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountProfile',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.account')),
                ('account_name', models.CharField(max_length=100)),
                ('account_nickname', models.CharField(max_length=100)),
                ('phone_num', models.CharField(blank=True, max_length=20, null=True)),
                ('account_add', models.CharField(blank=True, max_length=255, null=True)),
                ('account_sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('account_birth', models.DateField(blank=True, null=True)),
                ('account_pay', models.JSONField(blank=True, null=True)),
                ('account_sub', models.BooleanField(default=False)),
                ('account_age', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'account_profile',
            },
        ),
    ]
