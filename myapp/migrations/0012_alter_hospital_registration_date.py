# Generated by Django 5.0.6 on 2024-07-03 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_hospital_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='registration_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
