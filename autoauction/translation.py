from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Car)
class ProductTranslationOptions(TranslationOptions):
    fields = ('description',)