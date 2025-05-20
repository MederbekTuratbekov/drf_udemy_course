from rest_framework import generics, viewsets
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems
from .serializers import UserProfileSerializer, CategorySerializer, CourseSerializer, LessonSerializer, CertificateSerializer, ReviewSerializer, CartItemsSerializer, FavoriteItemsSerializer


class UserProfileViewSet(viewsets.ModelViewSet):
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

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class CertificateListApiView(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class ReviewListApiView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class CartItemsListApiView(generics.ListAPIView):
    queryset = CartItems.objects.all()
    serializer_class = CartItemsSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)

class FavoriteItemsListApiView(generics.ListAPIView):
    queryset = FavoriteItems.objects.all()
    serializer_class = FavoriteItemsSerializer

    def get_queryset(self):
        return UserProfile.objects.filter(id=self.request.user.id)
