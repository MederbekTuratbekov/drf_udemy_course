from rest_framework import serializers
from .models import UserProfile, Category, Course, Lesson, Certificate, Review, CartItems, FavoriteItems, Exam, Questions, Options, Assignment
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return UserProfile.objects.create_user(**validated_data)

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
        fields = ('id', 'category_name')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'lesson_title', 'video_url', 'content']


class CreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_image', 'category', 'course_name', 'price', 'author', 'course_description', 'level')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'course_image', 'category', 'course_name', 'price', 'author', 'course_description', 'level')


class CourseDetailSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    created_at = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Course
        fields = ('id', 'course_name', 'price', 'author', 'course_description', 'level', 'certificate_have', 'course_language', 'created_at', 'lessons')


class AssignmentSerializer(serializers.ModelSerializer):
    students = UserProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    due_date = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Assignment
        fields = ('id', 'assignment_title', 'assignment_description', 'due_date', 'course', 'students')


class OptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Options
        fields = ['id', 'option_text', 'is_correct']


class QuestionSerializer(serializers.ModelSerializer):
    options = OptionsSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['id', 'question_text', 'options']


class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_title']


class ExamDetailSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['id', 'exam_title', 'questions', 'passing_score', 'course', 'duration']


class CertificateSerializer(serializers.ModelSerializer):
    student = UserProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    issued_at = serializers.DateField(format='%d-%m-%Y')

    class Meta:
        model = Certificate
        fields = ['id', 'student', 'course', 'issued_at', 'certificate']


class ReviewSerializer(serializers.ModelSerializer):
    owner_review = UserProfileSerializer(read_only=True)
    course = CourseSerializer(read_only=True)
    review_created = serializers.DateTimeField(format='%d-%m-%Y %H:%M')

    class Meta:
        model = Review
        fields = ['id', 'owner_review', 'course', 'rating', 'comment', 'review_created']


class ReviewCreateSerializer(serializers.ModelSerializer):
    review_created = serializers.DateTimeField(format='%d-%m-%Y %H:%M', read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'owner_review', 'course', 'rating', 'comment', 'review_created']


class CartItemsSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = CartItems
        fields = ['id', 'cart', 'course']


class FavoriteItemsSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = FavoriteItems
        fields = ['id', 'favorite', 'course']