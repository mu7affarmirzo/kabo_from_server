# Generated by Django 2.2 on 2021-09-06 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_pagetitlemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitlemodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='pagetitlemodel',
            name='name_he',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='pagetitlemodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
