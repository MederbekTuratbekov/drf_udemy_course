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

class Network(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=30, blank=True, null=True)
    network_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.network_name

class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.category_name

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
    # created_at = models.DateField()

    def __str__(self):
        return f'{self.course_name}: {self.price}'

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=50)
    video_url = models.FileField(upload_to='video_urls/')
    content = models.FileField(upload_to='contents_lesson/')
    course = models.URLField()

    def __str__(self):
        return self.lesson_title

class Assignment(models.Model):
    assignment_title = models.TextField()
    assignment_description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.assignment_title

class Exam(models.Model):
    exam_name = models.TextField()
    course = models.ManyToManyField(Course)
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    duration = models.DurationField()

    def __str__(self):
        return self.exam_name

class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

class Options(models.Model):
    questions = models.ForeignKey(Options, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=30)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.option_text

class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField()

    def __str__(self):
        return 'It is Certificates'

class Review(models.Model):
    owner_review = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    review_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.rating} - {self.comment}'

class Cart(models.Model):
    cart_owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart_owner}'

class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course

class Favorite(models.Model):
    favorite_owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.favorite_owner}'

class FavoriteItems(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course
