from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(AwardsModel)
class AwardsTranslationOptions(TranslationOptions):
    fields = ('name', 'created_at')
