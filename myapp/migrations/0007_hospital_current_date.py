# Generated by Django 5.0.6 on 2024-06-25 08:47

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_hospital_subscript'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='current_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
