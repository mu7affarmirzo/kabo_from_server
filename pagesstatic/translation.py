from modeltranslation.translator import translator, TranslationOptions, register
from pagesstatic.models import LeadersModel, BannerModel

@register(LeadersModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'position')

@register(BannerModel)
class BannerTranslationOptions(TranslationOptions):
    fields = ('name','slang')