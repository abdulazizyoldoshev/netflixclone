from modeltranslation.translator import register, TranslationOptions
from .models import MoviesModel, CategoryModel


@register(MoviesModel)
class NewsTranslationOptions(TranslationOptions):
    fields = ('name', 'presented_description', 'detailed_description')


@register(CategoryModel)
class CategoryNewsTranslationOptions(TranslationOptions):
    fields = ('category_name', 'created_at')
