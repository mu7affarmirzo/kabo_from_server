# Generated by Django 2.2 on 2021-08-31 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0007_auto_20210831_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='missionmodel',
            old_name='header_de',
            new_name='header_he',
        ),
        migrations.RenameField(
            model_name='missionmodel',
            old_name='text_de',
            new_name='text_he',
        ),
        migrations.RenameField(
            model_name='missionmodel',
            old_name='title_de',
            new_name='title_he',
        ),
        migrations.RenameField(
            model_name='pagetitlemodel',
            old_name='title_de',
            new_name='title_he',
        ),
        migrations.RenameField(
            model_name='statisticsmodel',
            old_name='title_de',
            new_name='title_he',
        ),
    ]
