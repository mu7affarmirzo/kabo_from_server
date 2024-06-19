from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PageTitleModel)
class TitleTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )

@register(AboutUSModel)
class AboutUsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(StatisticsModel)
class StatisticsTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )

@register(MissionModel)
class MissionTranslationOptions(TranslationOptions):
    fields = (
        'header',
        'title',
        'text',
    )


@register(CompanyMissionModel)
class CMissionTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(TeamModel)
class TeamTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'position'
    )


@register(VacancyModel)
class VacancyTranslationOptions(TranslationOptions):
    fields = (
        'little_description',
        'position',
        'description',
        'requirements',
    )


@register(PartnersModel)
class PartnersTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'position',
        'description',
    )


@register(DownloadsModel)
class DownloadsTranslationOptions(TranslationOptions):
    fields = (
        'pre_title',
        'full_name',
        'description',
    )