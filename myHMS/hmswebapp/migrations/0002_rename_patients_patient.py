# Generated by Django 4.1.1 on 2022-09-17 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hmswebapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patients',
            new_name='Patient',
        ),
    ]