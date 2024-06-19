# Generated by Django 2.2 on 2021-09-15 09:53

import abcompany.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abcompany', '0022_sendresumemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('name_en', models.CharField(blank=True, max_length=150, null=True)),
                ('name_he', models.CharField(blank=True, max_length=150, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=150, null=True)),
                ('position', models.CharField(blank=True, max_length=150, null=True)),
                ('position_en', models.CharField(blank=True, max_length=150, null=True)),
                ('position_he', models.CharField(blank=True, max_length=150, null=True)),
                ('position_ru', models.CharField(blank=True, max_length=150, null=True)),
                ('description', ckeditor.fields.RichTextField()),
                ('description_en', ckeditor.fields.RichTextField(null=True)),
                ('description_he', ckeditor.fields.RichTextField(null=True)),
                ('description_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=abcompany.models.team_upload_location)),
            ],
            options={
                'verbose_name': 'Partners',
                'verbose_name_plural': 'Partners',
            },
        ),
        migrations.AlterModelOptions(
            name='sendresumemodel',
            options={'verbose_name': 'Arrived Resume/CVs', 'verbose_name_plural': 'Arrived Resume/CVs'},
        ),
    ]
