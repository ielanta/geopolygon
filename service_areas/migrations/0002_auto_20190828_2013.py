# Generated by Django 2.2.4 on 2019-08-28 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service_areas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicearea',
            old_name='service',
            new_name='provider',
        ),
    ]