from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PageTitleModel)
class TitleTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(NewsModel)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'text',
    )

