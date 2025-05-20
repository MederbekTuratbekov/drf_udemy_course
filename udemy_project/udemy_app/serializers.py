from rest_framework import serializers
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems, Exam
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('username', 'email', 'password', 'first_name', 'last_name',
#                   'age', 'phone_number', 'status', 'date_registered')
#         extra_kwargs = {'password': {'write_only': True}}
#
#     def create(self, validated_data):
#         user = UserProfile.objects.create_user(**validated_data)
#         return user
#
#     def to_representation(self, instance):
#         refresh = RefreshToken.for_user(instance)
#         return {
#             'user': {
#                 'username': instance.username,
#                 'email': instance.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }
#
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField(write_only=True)
#
#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Неверные учетные данные")
#
#     def to_representation(self, instance):
#         refresh = RefreshToken.for_user(instance)
#         return {
#             'user': {
#                 'username': instance.username,
#                 'email': instance.email,
#             },
#             'access': str(refresh.access_token),
#             'refresh': str(refresh),
#         }
# -----------------------------------------------------------------------------------------------
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
