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
    file_path = 'files/news/{title}-{filename}'.format(
                title=str(instance.title or instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


def team_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'files/news/{name}-{filename}'.format(
                name=str(instance.name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


def vacancy_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'files/vacancy/{position}-{filename}'.format(
                position=str(instance.position), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


def file_upload_location(instance, filename):
    ext = filename.split('.')[-1]
    file_path = 'files/{full_name}-{filename}'.format(
                full_name=str(instance.full_name), filename='{}.{}'.format(uuid4().hex, ext))
    return file_path


class PageTitleModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    page_promo = models.FileField(upload_to=upload_location, blank=True, null=True)

    @property
    def promoURL(self):
        try:
            url = self.page_promo.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title


class StatisticsModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    numbers = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.title


class MissionModel(models.Model):
    header = models.CharField(max_length=150, null=True, blank=True)
    title = models.CharField(max_length=150, null=True, blank=True)
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Missions and plans'
        verbose_name_plural = 'Missions and plans'


class CompanyMissionModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    page_promo = models.FileField(upload_to=upload_location, blank=True, null=True)
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'Missions of the company'
        verbose_name_plural = 'Missions of the company'

    def __str__(self):
        return self.title

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class TeamModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to=team_upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'Our Team'
        verbose_name_plural = 'Our Team'

    def __str__(self):
        return self.name

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class PartnersModel(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to=team_upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'Partners'
        verbose_name_plural = 'Partners'

    def __str__(self):
        return self.name

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class AboutUSModel(models.Model):
    title = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextField()
    image = models.ImageField(upload_to=upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'About Us'
        verbose_name_plural = 'About Us'

    def __str__(self):
        return self.title

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class VacancyModel(models.Model):
    little_description = models.CharField(max_length=150, null=True, blank=True)
    position = models.CharField(max_length=150, null=True, blank=True)
    description = RichTextField()
    requirements = models.CharField(max_length=150, null=True, blank=True)
    image = models.ImageField(upload_to=vacancy_upload_location, blank=True, null=True)
    slug = models.SlugField(blank=True, unique=True)

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Vacancy'

    def __str__(self):
        return str(self.position)

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class DownloadsModel(models.Model):
    pre_title = models.CharField(max_length=150, null=True, blank=True)
    full_name = models.CharField(max_length=150, null=True, blank=True)
    description = models.CharField(max_length=150, null=True, blank=True)
    file = models.FileField(upload_to=file_upload_location, null=True, blank=True)
    image = models.ImageField(upload_to=file_upload_location, blank=True, null=True)

    class Meta:
        verbose_name = 'Download files'
        verbose_name_plural = 'Download files'

    def __str__(self):
        return str(self.full_name)

    def fileUrl(self):
        try:
            url = self.file.url
        except:
            url = ''
        return url

    def imageUrl(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class SendResumeModel(models.Model):
    full_name = models.CharField(max_length=150, null=True, blank=True)
    phone_number = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    cv = models.FileField(upload_to=file_upload_location, null=True, blank=True)

    class Meta:
        verbose_name = "Arrived Resume/CVs"
        verbose_name_plural = "Arrived Resume/CVs"

    def __str__(self):
        return self.full_name


@receiver(post_delete, sender=SendResumeModel)
def file_submission_delete(sender, instance, **kwargs):
    instance.cv.delete(False)


@receiver(post_delete, sender=VacancyModel)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)


def pre_save_vacancies_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(r.randint(1,10000)) + "-" + str(r.randint(1,10000)))


pre_save.connect(pre_save_vacancies_post_receiver, sender=VacancyModel)