from rest_framework import serializers
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems, Exam, Questions, Options
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

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

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'lesson_title', 'video_url', 'content', 'course']

class CourseDetailSerializer(serializers.ModelSerializer):
    lesson_title = LessonSerializer(many=True, read_only=True)
    video_url = LessonSerializer(many=True, read_only=True)
    content = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ('id', 'course_name', 'price', 'author', 'course_description', 'level', 'certificate_have', 'course_lenguage', 'created_at', 'lesson_title',  'video_url', 'content')

class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'option_text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True, source='options_set')
    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'options']

class ExamenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_title']

class ExamenDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True, source='questions_set')
    class Meta:
        model = Exam
        fields = ['id', 'exam_title', 'questions', 'passing_score', 'course', 'duration']

class CertificateSerializer(serializers.ModelSerializer):
    students = UserProfileSerializer(read_only=True)
    course = UserProfileSerializer(read_only=True)
    certificate = UserProfileSerializer(read_only=True)
    class Meta:
        model = Certificate
        fields = ['id', 'students', 'course', 'issued_at', 'certificate']

class ReviewSerializer(serializers.ModelSerializer):
    owner_review = UserProfileSerializer(read_only=True)
    course = UserProfileSerializer(read_only=True)
    rating = UserProfileSerializer(read_only=True)
    comment = UserProfileSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ['id', 'owner_review', 'course', 'rating', 'comment', 'review_created']

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'owner_review', 'course', 'rating', 'comment', 'review_created']

class CartItemsSerializer(serializers.ModelSerializer):
    course = UserProfileSerializer(read_only=True)
    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'course']

class FavoriteItemsSerializer(serializers.ModelSerializer):
    course = UserProfileSerializer(read_only=True)
    class Meta:
        model = FavoriteItems
        fields = ['id', 'favorite', 'course']
