from tkinter.font import names

from django.urls import path, include
from rest_framework import routers
from .views import RegisterView, CustomLoginView, LogoutView
from .views import (UserProfileListAPIView, UserProfileDetailListAPIView, CategoryListAPIView, ExamListApiView, ExamDetailListApiView,
                    CourseListApiView, CourseDetailListApiView, ReviewViewSet, LessonListApiView, CertificateListApiView, CreateCourseViewSet,
                    ReviewListApiView, CartItemsListApiView, FavoriteItemsListApiView, AssignmentListApiView)


router = routers.SimpleRouter()
router.register(r'create_review', ReviewViewSet, basename='review_crud')
router.register(r'create_course', CreateCourseViewSet, basename='course_crud')


urlpatterns = [

    path('', include(router.urls)),

    path('user/', UserProfileListAPIView.as_view(), name = 'users'),
    path('user/<int:pk>/', UserProfileDetailListAPIView.as_view(), name = 'user_detail'),

    path('assignment/', AssignmentListApiView.as_view(), name = 'assignments'),

    path('category_list/', CategoryListAPIView.as_view(), name= 'category_list'),

    path('course/', CourseListApiView.as_view(), name= 'course_list'),
    path('course/<int:pk>/', CourseDetailListApiView.as_view(), name='course_detail'),

    path('exam/', ExamListApiView.as_view(), name = 'exam_list'),
    path('exam/<int:pk>/', ExamDetailListApiView.as_view(), name = 'exam_detail'),

    path('lessons/', LessonListApiView.as_view(), name='lesson_list'),

    path('certificates/', CertificateListApiView.as_view(), name='certificate_list'),

    path('reviews/', ReviewListApiView.as_view(), name='review_list'),

    path('cart-items/', CartItemsListApiView.as_view(), name='cart_items_list'),

    path('favorite-items/', FavoriteItemsListApiView.as_view(), name='favorite_items_list'),

    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(), name = 'logout'),
]
