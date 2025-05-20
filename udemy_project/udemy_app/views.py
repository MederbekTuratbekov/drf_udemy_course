from rest_framework import generics, viewsets
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems
from .serializers import (UserProfileSerializer, UserProfileDetailSerializer, CategorySerializer,
                          CourseSerializer, CourseDetailSerializer, LessonSerializer, CertificateSerializer,
                          ReviewSerializer, CartItemsSerializer, FavoriteItemsSerializer,
                          ExamenSerializer, ExamenDetailSerializer)


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class UserProfileDetailListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer

class ExamListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = ExamenSerializer

class ExamDetailListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = ExamenDetailSerializer

class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CertificateListApiView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class ReviewListApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CartItemsListApiView(generics.ListAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer

class FavoriteItemsListApiView(generics.ListAPIView):
    queryset = FavoriteItems.objects.all()
    serializer_class = FavoriteItemsSerializer
