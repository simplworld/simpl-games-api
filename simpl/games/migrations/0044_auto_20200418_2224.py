# Generated by Django 2.2.12 on 2020-04-18 22:24

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0043_auto_20200418_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decision',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict),
        ),
    ]
