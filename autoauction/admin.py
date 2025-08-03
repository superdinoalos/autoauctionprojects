from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class CarImageInline(admin.TabularInline):
    model = CarImages
    extra = 1

@admin.register(Car)
class ProductAdmin(TranslationAdmin):
    inlines = [CarImageInline]

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(UserProfile)
admin.site.register(Brand)
admin.site.register(Model)
admin.site.register(CarImages)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Feedback)
