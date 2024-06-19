from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(PageTitleModel)
class TitleTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )


@register(ProjectModel)
class ProjectTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'text',
        'company_name',
    )

@register(MiniBlockModel)
class MiniBlocksTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'text',
        'company_name',
    )
