from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin

# Register your models here.
# *************************ProjectModel*************************
class ProjectCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Our projects"


class ProjectAdmin(ProjectCustomAdmin, TranslationAdmin):
    pass


admin.site.register(ProjectModel, ProjectAdmin)


# *************************PageTitleModel*************************
class TitleCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Page Title"


class TitleAdmin(TitleCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PageTitleModel, TitleAdmin)


# *************************MiniBlockModel*************************
class BlockCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Project blocks"


class BlocksAdmin(BlockCustomAdmin, TranslationAdmin):
    pass


admin.site.register(MiniBlockModel, BlocksAdmin)
