# Generated by Django 2.1.4 on 2018-12-13 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='utilisateurs',
            old_name='uti_id',
            new_name='tel',
        ),
    ]
