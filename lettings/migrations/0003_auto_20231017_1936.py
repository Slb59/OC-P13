# Generated by Django 3.0 on 2023-10-17 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0002_data_from_oc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Addresses'},
        ),
    ]