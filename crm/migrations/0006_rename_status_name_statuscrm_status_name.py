# Generated by Django 3.2.12 on 2022-11-15 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0005_auto_20201119_1539'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statuscrm',
            old_name='Status_name',
            new_name='status_name',
        ),
    ]
