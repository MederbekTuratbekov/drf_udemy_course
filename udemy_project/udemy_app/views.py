from rest_framework import generics, viewsets, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework import permissions
from .permissions import *
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems, Exam
from .serializers import (UserSerializer, LoginSerializer, UserProfileSerializer, UserProfileDetailSerializer, CategorySerializer,
                          CourseSerializer, CourseDetailSerializer, LessonSerializer, CertificateSerializer, ReviewCreateSerializer,
                          ReviewSerializer, CartItemsSerializer, FavoriteItemsSerializer,
                          ExamenSerializer, ExamenDetailSerializer)


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class CustomLoginView(TokenObtainPairView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except Exception:
            return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)

        user = serializer.validated_data
        return Response(serializer.data, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)
# -----------------------------------------------------------------------------------------------
class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class UserProfileDetailListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    search_fields = ['category', 'course_name', ]
    filterset_fields = ['level']
    ordering_fields = ['certificate_have', 'level']
    ordering = ['level']

class CourseDetailListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class ExamListApiView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamenSerializer

class ExamDetailListApiView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamenDetailSerializer

class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

    permission_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     return Lesson.objects.filter(author = self.request.user)

class CertificateListApiView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class ReviewListApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewCreateSerializer

    permission_classes = [permissions.IsAuthenticated, CreatePermissions]

class CartItemsListApiView(generics.ListAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class FavoriteItemsListApiView(generics.ListAPIView):
    queryset = FavoriteItems.objects.all()
    serializer_class = FavoriteItemsSerializer

    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)
