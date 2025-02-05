# Generated by Django 2.2 on 2021-10-30 15:50

import abcompany.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0026_downloadsmodel_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUSModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=abcompany.models.team_upload_location)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
    ]
