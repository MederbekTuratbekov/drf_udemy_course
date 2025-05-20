from rest_framework import generics
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems
from .serializers import UserProfileSerializer, CategorySerializer, CourseSerializer, LessonSerializer, CertificateSerializer, ReviewSerializer, CartItemsSerializer, FavoriteItemsSerializer


class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CourseListApiView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class LessonListApiView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class CertificateListApiView(generics.ListAPIView):
    queryset = Certificate
    serializer_class = CertificateSerializer

class ReviewListApiView(generics.ListAPIView):
    queryset = Review
    serializer_class = ReviewSerializer

class CartItemsListApiView(generics.ListAPIView):
    queryset = CartItems
    serializer_class = CartItemsSerializer

class FavoriteItemsListApiView(generics.ListAPIView):
    queryset = FavoriteItems
    serializer_class = FavoriteItemsSerializer
