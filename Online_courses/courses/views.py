from rest_framework import viewsets, generics, permissions, status
from .serializers import *
from .permissions import CheckCreateCourse, CheckEditCourse, CheckReview, CheckCertificate, CheckCreateLesson
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import  SearchFilter
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView



class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer =self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data,  status=status.HTTP_201_CREATED)



class CustomLoginView(TokenObtainPairView):
    serializer_class =LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status = status.HTTP_200_OK)



class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs ):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)



class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['category']
    search_fields  = ['course_name']



class CourseDetailApiView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer



class CourseCreateApiView(generics.CreateAPIView):
    serializer_class = CourseCreateSerializer
    permission_classes = [CheckCreateCourse]



class CourseUpdateDeleteApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreateSerializer
    permission_classes = [CheckEditCourse]



class LessonCreateApiView(generics.CreateAPIView):
    serializer_class = LessonCreateSerializer
    permission_classes = [CheckCreateLesson]



class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer



class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.all()
    serializer_class = ExamSerializer



class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer



class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    permission_classes = [CheckCertificate]



class CourseReviewApiView(generics.ListAPIView):
    queryset = CourseReview.objects.all()
    serializer_class = CourseReviewSerializer



class CourseReviewCreateApiView(generics.CreateAPIView):
    serializer_class = CourseReviewSerializer
    permission_classes = [CheckReview]



class TeacherReviewApiView(generics.ListAPIView):
    queryset = TeacherReview.objects.all()
    serializer_class = TeacherReviewSerializer



class TeacherReviewCreateApiView(generics.CreateAPIView):
    serializer_class = TeacherReviewSerializer
    permission_classes = [CheckReview]