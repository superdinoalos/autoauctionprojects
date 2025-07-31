from django.contrib import admin
from .models import *
<<<<<<< HEAD

admin.site.register(UserProfile)
admin.site.register(Car)
admin.site.register(Auction)
admin.site.register(Bid)
admin.site.register(Feedback)

=======
from modeltranslation.admin import TranslationAdmin


@admin.register(Car)
class CountryAdmin(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
