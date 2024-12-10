from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


@admin.register(Course)
class CourseAdmin(TranslationAdmin):
    pass


admin.site.register(UserProfile)
admin.site.register(Lesson)
admin.site.register(Category)
admin.site.register(Certificate)
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(CourseReview)
admin.site.register(TeacherReview)
