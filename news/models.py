from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from datetime import datetime
from django.dispatch import receiver
from django.db.models.signals import post_delete
from uuid import uuid4

import random as r


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'files/news-archive/{name}-{filename}'.format(
                name=str(instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PageTitleModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    page_promo = models.FileField(upload_to=upload_location, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    @property
    def promoURL(self):
        try:
            url = self.page_promo.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Page Title'
        verbose_name_plural = 'Page Title'


class NewsModel(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)
    text = RichTextField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True, verbose_name="date_published")
    slug = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'


@receiver(post_delete, sender=NewsModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_news_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))


pre_save.connect(pre_save_news_post_receiver, sender=NewsModel)
