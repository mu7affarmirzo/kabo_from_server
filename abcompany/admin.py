from django.contrib import admin

from .models import *
from modeltranslation.admin import TranslationAdmin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from django.contrib.admin.models import LogEntry
# entries = LogEntry.objects.all()

# admin.site.register(LogEntry)

# *************************AboutUsModel*************************
class AboutUsCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "About Us"


class AboutUsAdmin(AboutUsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(AboutUSModel, AboutUsAdmin)


# *************************PageTitleModel*************************
class TitleCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Page Title"


class TitleAdmin(TitleCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PageTitleModel, TitleAdmin)


# *************************StatisticsModel*************************
class StatisticsCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Statistics"


class StatisticsAdmin(StatisticsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(StatisticsModel, StatisticsAdmin)


# *************************MissionModel*************************
class MissionCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Missions"


class MissionAdmin(MissionCustomAdmin, TranslationAdmin):
    pass


admin.site.register(MissionModel, MissionAdmin)


# *************************CompanyMissionModel*************************
class CMissionCustomAdmin(admin.ModelAdmin):
    list_display = ('title_he', 'title_en', 'title_ru')

    class Meta:
        verbose_name = "Company Mission"


class CMissionAdmin(CMissionCustomAdmin, TranslationAdmin):
    pass


admin.site.register(CompanyMissionModel, CMissionAdmin)


# *************************TeamModel*************************
class TeamCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Our Team"


class TeamAdmin(TeamCustomAdmin, TranslationAdmin):
    pass


admin.site.register(TeamModel, TeamAdmin)


# *************************VacancyModel*************************
class VacancyCustomAdmin(admin.ModelAdmin):
    list_display = ('position_he', 'position_en', 'position_ru')

    class Meta:
        verbose_name = "Vacancy"


class VacancyAdmin(VacancyCustomAdmin, TranslationAdmin):
    pass


admin.site.register(VacancyModel, VacancyAdmin)

admin.site.register(SendResumeModel)


# *************************PartnersModel*************************
class PartnersCustomAdmin(admin.ModelAdmin):
    list_display = ('name_he', 'name_en', 'name_ru')

    class Meta:
        verbose_name = "Partners"


class PartnersAdmin(PartnersCustomAdmin, TranslationAdmin):
    pass


admin.site.register(PartnersModel, PartnersAdmin)


# *************************DownloadsModel*************************
class DownloadsCustomAdmin(admin.ModelAdmin):
    list_display = ('full_name_he', 'full_name_en', 'full_name_ru')

    class Meta:
        verbose_name = "Download files"


class DownloadsAdmin(DownloadsCustomAdmin, TranslationAdmin):
    pass


admin.site.register(DownloadsModel, DownloadsAdmin)
