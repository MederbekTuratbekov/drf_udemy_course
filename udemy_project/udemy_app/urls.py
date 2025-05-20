from rest_framework import routers
from django.urls import path, include
from .views import (StudentProfileListAPIView, TeacherProfileViewSet, CategoryListAPIView, CourseListApiView, LessonListApiView, CertificateListApiView,
                    ReviewListApiView, CartItemsListApiView, FavoriteItemsListApiView)


router = routers.SimpleRouter()
router.register(r'teacher_account/', TeacherProfileViewSet, basename='teacher_account') # не работает


urlpatterns = [
    path('student_account/', StudentProfileListAPIView.as_view(), name = 'student_accounts'),
    path('category_list', CategoryListAPIView.as_view(), name='category_list'),
    path('', CourseListApiView.as_view(), name='course_list'),
    path('lessons/', LessonListApiView.as_view(), name='lesson_list'),
    path('certificates/', CertificateListApiView.as_view(), name='certificate_list'),
    path('reviews/', ReviewListApiView.as_view(), name='review_list'),
    path('cart_items/', CartItemsListApiView.as_view(), name='cart_items_list'),
    path('favorite_items/', FavoriteItemsListApiView.as_view(), name='favorite_items_list'),
]
