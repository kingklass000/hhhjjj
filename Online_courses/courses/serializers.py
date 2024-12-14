from django.contrib.auth import authenticate
from rest_framework import  serializers
from rest_framework_simplejwt.tokens import RefreshToken
from .models import *



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email','password' ]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
            user = UserProfile.objects.create_user(**validated_data)
            return user



class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }



class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'



class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name']



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']



class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content']



class LessonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'video_url', 'content', 'course']



class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['course_name']



class CourseListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'image', 'category' , 'avg_rating', 'count_people']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


    def get_count_people(self, obj):
        return obj.get_count_people()



class CourseDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    owner = UserProfileSimpleSerializer()
    course_content = LessonSerializer(many=True, read_only=True)
    created_by = serializers.DateTimeField(format= '%d-%m-%Y   %H:%M' )
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'image', 'category', 'description', 'level', 'price', 'created_by', 'course_content', 'owner', 'avg_rating', 'count_people']


    def get_avg_rating(self, obj):
        return obj.get_avg_rating()


    def get_count_people(self, obj):
        return obj.get_count_people()



class CourseCreateSerializer(serializers.ModelSerializer):
    course_content = LessonSerializer()
    class Meta:
        model = Course
        fields = ['course_name', 'image', 'category', 'description', 'level', 'price', 'course_content', 'created_by', 'owner']



class AssignmentSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    student = UserProfileSimpleSerializer()
    due_date = serializers.DateTimeField(format='%d-%m-%Y   %H:%M')
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due_date', 'course', 'student']



class ExamSerializer(serializers.ModelSerializer):
    course = CourseSimpleSerializer()
    student  = UserProfileSimpleSerializer()
    duration = serializers.DateTimeField(format= '%d-%m-%Y   %H:%M')
    class Meta:
        model = Exam
        fields = ['title', 'course', 'passing_score', 'duration', 'student']



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['question']



class CertificateSerializer(serializers.ModelSerializer):
    student = UserProfileSimpleSerializer()
    course = CourseSimpleSerializer()
    issued_at = serializers.DateTimeField(format='%d-%m-%Y   %H:%M')
    class Meta:
        model = Certificate
        fields = ['student', 'course', 'issued_at', 'certificate_url']



class CourseReviewSerializer(serializers.ModelSerializer):
    user = UserProfileSimpleSerializer()
    course = CourseSimpleSerializer()
    class Meta:
        model = CourseReview
        fields = ['user', 'course', 'rating', 'comment']



class TeacherReviewSerializer(serializers.ModelSerializer):
    user  = UserProfileSimpleSerializer()
    teacher  = UserProfileSimpleSerializer()
    class Meta:
        model = TeacherReview
        fields =['user', 'teacher', 'rating', 'comment']