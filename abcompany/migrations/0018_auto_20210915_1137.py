# Generated by Django 2.2 on 2021-09-15 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0017_auto_20210915_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancymodel',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
