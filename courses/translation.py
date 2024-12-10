from .models import Course
from modeltranslation.translator import TranslationOptions,register

@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')
