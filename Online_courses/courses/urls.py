from django.urls import path, include
from rest_framework import routers
from .views import *



router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'assignment', AssignmentViewSet, basename='assignment')
router.register(r'exam', ExamViewSet, basename='exam')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'certificate', CertificateViewSet, basename='certificate')



urlpatterns = [
    path('', include(router.urls)),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('course', CourseListApiView.as_view(), name = 'course_list'),
    path('course/<int:pk>/', CourseDetailApiView.as_view(), name = 'course_detail'),
    path('course/create', CourseCreateApiView.as_view(), name = 'course_create'),
    path('course/create/<int:pk>/', CourseUpdateDeleteApiView.as_view(), name = 'course_edit'),
    path('course/lesson_create/', LessonCreateApiView.as_view(), name = 'create_lesson'),
    path('course/review/', CourseReviewApiView.as_view(), name = 'course_reviews'),
    path('course/review/create/', CourseReviewCreateApiView.as_view(), name = 'course_review_create'),
    path('course/teacher_review/', TeacherReviewApiView.as_view(), name = 'teacher_reviews'),
    path('course/teacher_review/create/', TeacherReviewCreateApiView.as_view(), name = 'teacher_review_create')
]