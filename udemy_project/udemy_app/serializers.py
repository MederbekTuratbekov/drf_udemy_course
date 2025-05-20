from rest_framework import serializers
from models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'last_name', 'first_name', 'email', 'password', 'role', 'full_name', 'profile_picture', 'bio']
        extra_kwargs = {'password': {'write_only': True}}
        # full name, bio

    # def full_name(self):
    #     return f'{self.last_name} {self.first_name}'

    # def bio(self, request):
    #     if request.id == UserProfile.role.teacher:

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_name',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('category', 'course_name', 'course_description', 'level', 'price', 'created_by')

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['course', 'lesson_title', 'video_url', 'content', 'course']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['students', 'course', 'issued_at', 'certificate_url']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['owner_review', 'course', 'rating', 'comment', 'review_created']

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['cart', 'course']

class FavoriteItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItems
        fields = ['favorite', 'course']