from rest_framework import generics, viewsets
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems
from .serializers import StudentAccountSerializer, TeacherAccountSerializer, CategorySerializer, CourseSerializer, LessonSerializer, CertificateSerializer, ReviewSerializer, CartItemsSerializer, FavoriteItemsSerializer


class StudentProfileListAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = StudentAccountSerializer

    # def get_queryset(self):
    #     return UserProfile.objects.filter(id=self.request.user.id)

class TeacherProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = TeacherAccountSerializer

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
