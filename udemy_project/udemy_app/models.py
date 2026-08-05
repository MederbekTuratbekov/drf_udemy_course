from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} - {self.role}'


class Network(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    network_name = models.CharField(max_length=30, blank=True, null=True)
    network_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.network_name}'


class Category(models.Model):
    category_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.category_name}'


class Course(models.Model):
    LEVEL_CHOICES = (
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    PRICE_TYPE_CHOICES = (
        ('paid', 'Paid'),
        ('free', 'Free'),
    )
    LANGUAGE_CHOICES = (
        ('English', 'English'),
        ('Russian', 'Russian'),
    )

    course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    category = models.ManyToManyField(Category)
    course_name = models.CharField(max_length=50)
    course_description = models.TextField()
    level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
    price = models.PositiveIntegerField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    is_free = models.CharField(max_length=10, choices=PRICE_TYPE_CHOICES, default='paid')
    certificate_have = models.BooleanField(default=True)
    course_language = models.CharField(max_length=20, choices=LANGUAGE_CHOICES, default='English')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.course_name}: {self.price} $'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    lesson_title = models.CharField(max_length=50)
    video_url = models.URLField()
    content = models.FileField(upload_to='contents_lesson/', blank=True, null=True)

    def __str__(self):
        return f'{self.lesson_title}'


class Assignment(models.Model):
    assignment_title = models.TextField()
    assignment_description = models.TextField()
    due_date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    students = models.ManyToManyField(UserProfile)

    def __str__(self):
        return f'{self.assignment_title}'


class Exam(models.Model):
    exam_title = models.CharField(max_length=50)
    course = models.ManyToManyField(Course)
    passing_score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    duration = models.TimeField()

    def __str__(self):
        return f'{self.exam_title}'


class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions')
    question_text = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.question_text}'


class Options(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options')
    option_text = models.CharField(max_length=100, blank=True, null=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.option_text}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate = models.FileField()

    def __str__(self):
        return f'Certificate of: {self.student}'


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
        return f'Cart of: {self.cart_owner}'


class CartItems(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}'


class Favorite(models.Model):
    favorite_owner = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'Favorite of: {self.favorite_owner}'


class FavoriteItems(models.Model):
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}'


@receiver(post_save, sender=UserProfile)
def create_cart_and_favorite(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(cart_owner=instance)
        Favorite.objects.create(favorite_owner=instance)
