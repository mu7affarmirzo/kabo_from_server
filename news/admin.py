from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
# *************************ProjectModel*************************
class NewsCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru', 'date_published')

    class Meta:
        verbose_name = "News"


class NewsAdmin(NewsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(NewsModel, NewsAdmin)


# *************************PageTitleModel*************************
class TitleCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Page Title"


class TitleAdmin(TitleCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PageTitleModel, TitleAdmin)


