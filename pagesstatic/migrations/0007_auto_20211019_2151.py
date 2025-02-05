# Generated by Django 2.2 on 2021-10-19 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagesstatic', '0006_auto_20211019_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannermodel',
            name='slang',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='slang_en',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='slang_he',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='bannermodel',
            name='slang_ru',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='name',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='name_en',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='name_he',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
        migrations.AlterField(
            model_name='bannermodel',
            name='name_ru',
            field=models.CharField(blank=True, max_length=350, null=True),
        ),
    ]
