from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin

# this is for ratingData
class BannerCustomAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_he', 'name_ru')
    class Meta:
        verbose_name = "Page Banner"
class BannerAdmin(BannerCustomAdmin, TranslationAdmin):
    pass
admin.site.register(BannerModel, BannerAdmin)

# admin.site.register(BannerModel)