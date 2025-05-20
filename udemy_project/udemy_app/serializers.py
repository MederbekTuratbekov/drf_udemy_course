from rest_framework import serializers
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems, Exam


# аккаунт студента
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'profile_picture']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'username', 'last_name', 'first_name', 'email', 'password', 'role']
        extra_kwargs = {'password': {'write_only': True}}

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'category_name',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_image', 'category', 'course_name', 'price', 'author', 'course_description', 'level')

class CourseDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'price', 'author', 'course_description', 'level', 'certificate_have', 'course_lenguage', 'created_at') # 'lesson_title',  'video_url', , 'content'

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('id', 'exam_title')

class ExamenDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ('exam_title', 'passing_score', 'course', 'duration') # 'question_text', 'option_text',

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'lesson_title', 'video_url', 'content', 'course']

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ['id', 'students', 'course', 'issued_at', 'certificate']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'owner_review', 'course', 'rating', 'comment', 'review_created']

class CartItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'course']

class FavoriteItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteItems
        fields = ['id', 'favorite', 'course']
