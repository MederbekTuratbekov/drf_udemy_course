from rest_framework import routers
from django.urls import path, include
from .views import (UserProfileViewSet, CategoryListAPIView, CourseListApiView, LessonListApiView, CertificateListApiView,
                    ReviewListApiView, CartItemsListApiView, FavoriteItemsListApiView)


router = routers.SimpleRouter()
router.register(r'users', UserProfileViewSet, basename='userprofile')


urlpatterns = [
    path('', include(router.urls)),
    path('categories/', CategoryListAPIView.as_view(), name='category_list'),
    path('courses/', CourseListApiView.as_view(), name='course_list'),
    path('lessons/', LessonListApiView.as_view(), name='lesson_list'),
    path('certificates/', CertificateListApiView.as_view(), name='certificate_list'),
    path('reviews/', ReviewListApiView.as_view(), name='review_list'),
    path('cart-items/', CartItemsListApiView.as_view(), name='cart_items_list'),
    path('favorite-items/', FavoriteItemsListApiView.as_view(), name='favorite_items_list'),
]
