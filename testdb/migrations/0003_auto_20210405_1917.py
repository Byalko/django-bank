# Generated by Django 3.1.7 on 2021-04-05 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testdb', '0002_auto_20210405_1914'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Card',
        ),
    ]
