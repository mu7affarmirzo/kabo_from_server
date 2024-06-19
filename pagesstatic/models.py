from django.db import models
from ckeditor.fields import RichTextField
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete
from uuid import uuid4

import random as r


def upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'about/{name}-{filename}'.format(
                name=str(instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class LeadersModel(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    position = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(upload_to=upload_location, null=True, blank=True)

    class Meta:
        ordering = ['-name']

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.name)


class BannerModel(models.Model):
    name = models.CharField(max_length=350, null=True, blank=True)
    slang = models.CharField(max_length=250, null=True, blank=True)
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
        verbose_name = 'Page banner'
        verbose_name_plural = 'Page banner'


@receiver(post_delete, sender=BannerModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)
    instance.page_promo.delete(False)