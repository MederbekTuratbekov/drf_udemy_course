from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    CHOICES_ROLE = (
        ('student', 'student'),
        ('teacher', 'teacher'))
    role = models.CharField(choices=CHOICES_ROLE, default='student')
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} - {self.role}'

# ссылки и их названия
class Network(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=30, blank=True, null=True)
    network_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.network_name

# категория курсов
class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name

# курс
class Course(models.Model):
    category = models.ManyToManyField(Category)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    CHOICES_LEVEL = (
        ('beginner', 'beginner'),
        ('intermedia', 'intermedia'),
        ('advanced', 'advanced'))
    level = models.CharField(choices=CHOICES_LEVEL)
    price = models.PositiveIntegerField()
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    # created_at = models.DateField() # агай озу коргозуп берем деген кандай реализация кылынаарын
    # updated_at =  # агай озу коргозуп берем деген кандай реализация кылынаарын

    def __str__(self):
        return f'{self.course_name}: {self.price}'

# урок курса
class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=50)
    video_url = models.FileField(upload_to='video_urls/')
    content = models.FileField(upload_to='contents_lesson/')
    course = models.URLField()

    def __str__(self):
        return self.lesson_title

# домашний задание
class Assignment(models.Model):
    assignment_title = models.TextField()
    assignment_description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment_title

# экзамен
class Exam(models.Model):
    exam_title = models.TextField()
    course = models.ManyToManyField(Course)
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    duration = models.TimeField()
    is_free = models.BooleanField() # платный/бесплатный

    def __str__(self):
        return self.exam_title

# вопросы экзамена
class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

# вариянты ответов вопроса
class Options(models.Model):
    questions = models.ForeignKey(Options, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=30)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text

# сертификат если успешно пройден курс
class Certificate(models.Model):
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField()

    def __str__(self):
        return 'It is Certificates'

# студенты могут оставить отзыв на курсы, но преподаватели не могут оставить отзыв на свой курс
class Review(models.Model):
    owner_review = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    review_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.comment}'

# корзину подключаем к владельцу корзины
class Cart(models.Model):
    cart_owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart_owner}'

# всё что есть в корзине
class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

# подключаем избранные(курсы) к пользователью
class Favorite(models.Model):
    favorite_owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite_owner}'

# все избранные курсы
class FavoriteItems(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course
