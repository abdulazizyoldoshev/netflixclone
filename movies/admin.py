from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


# Register your models here.


@admin.register(CategoryModel)
class CategoryModelAdmin(TranslationAdmin):
    list_display = ['id', 'category_name']
    list_display_link = ['id', 'category_name']
    list_filter = ['category_name']
    search_fields = ['id', 'category_name']

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(TagModel)
class TagModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    list_filter = ['name']
    search_fields = ['id', 'name']


@admin.register(MoviesModel)
class MoviesModelAdmin(TranslationAdmin):
    list_display = ['id', 'name', 'category', 'thumbnail_preview', 'thumbnail_preview_film']
    list_display_link = ['id', 'name', 'category']
    list_filter = ['name', 'year', 'category']
    search_fields = ['name', 'year', 'category', 'presented_description', 'detailed_description']
    autocomplete_fields = ['tag', 'category', 'director', 'screenplay', 'producer', 'award']
    readonly_fields = ['thumbnail_preview', 'thumbnail_preview_film']

    def thumbnail_preview(self, obj):
        return obj.thumbnail_preview

    thumbnail_preview.short_description = 'Thumbnail Preview'
    thumbnail_preview.allow_tags = True

    def thumbnail_preview_film(self, obj):
        return obj.thumbnail_preview_film

    thumbnail_preview_film.short_description = 'Thumbnail Preview Film'
    thumbnail_preview_film.allow_tags = True

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
