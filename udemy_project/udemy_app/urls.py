from django.urls import path, include
from rest_framework import routers
from .views import (RegisterView, CustomLoginView, LogoutView,
                    UserProfileListAPIView, UserProfileDetailListAPIView,
                    CategoryListAPIView, ExamListApiView, ExamDetailListApiView,
                    CourseListApiView, CourseDetailListApiView, ReviewViewSet,
                    LessonListApiView, CertificateListApiView, CreateCourseViewSet,
                    ReviewListApiView, CartItemsListApiView, FavoriteItemsListApiView,
                    AssignmentListApiView)

router = routers.SimpleRouter()
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'courses/manage', CreateCourseViewSet, basename='course-manage')

urlpatterns = [
    path('', include(router.urls)),

    path('users/', UserProfileListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailListAPIView.as_view(), name='user-detail'),

    path('assignments/', AssignmentListApiView.as_view(), name='assignment-list'),
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),

    path('courses/', CourseListApiView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetailListApiView.as_view(), name='course-detail'),

    path('exams/', ExamListApiView.as_view(), name='exam-list'),
    path('exams/<int:pk>/', ExamDetailListApiView.as_view(), name='exam-detail'),

    path('lessons/', LessonListApiView.as_view(), name='lesson-list'),
    path('certificates/', CertificateListApiView.as_view(), name='certificate-list'),
    path('reviews/all/', ReviewListApiView.as_view(), name='review-list'),

    path('cart-items/', CartItemsListApiView.as_view(), name='cart-items'),
    path('favorite-items/', FavoriteItemsListApiView.as_view(), name='favorite-items'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]