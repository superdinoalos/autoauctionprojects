from .models import UserProfile, Car
from modeltranslation.translator import TranslationOptions,register


@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    field = ('username',)


@register(Car)
class CarTranslationOptions(TranslationOptions):
    field = ('brand', 'description')


