from .models import Course,Category,  Lesson, Assignment, Exam, Question, CourseReview, TeacherReview
from modeltranslation.translator import TranslationOptions,register



@register(Course)
class ProductTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description')



@register(Category)
class ProductTranslationOptions(TranslationOptions):
    fields = ('category_name', )



@register(Lesson)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'content')



@register(Assignment)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description')



@register(Exam)
class ProductTranslationOptions(TranslationOptions):
    fields = ('title', )



@register(Question)
class ProductTranslationOptions(TranslationOptions):
    fields = ('question', )



@register(CourseReview)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment', )



@register(TeacherReview)
class ProductTranslationOptions(TranslationOptions):
    fields = ('comment', )