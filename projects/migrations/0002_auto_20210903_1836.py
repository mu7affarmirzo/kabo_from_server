# Generated by Django 2.2 on 2021-09-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagetitlemodel',
            name='title_en',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='pagetitlemodel',
            name='title_he',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='pagetitlemodel',
            name='title_ru',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='company_name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='company_name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='company_name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='name_he',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='text_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='text_he',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='projectmodel',
            name='text_ru',
            field=models.TextField(blank=True, null=True),
        ),
    ]
