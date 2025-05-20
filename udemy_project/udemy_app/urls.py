from rest_framework import routers
from django.urls import path, include
from .views import UserProfileListAPIView, CategoryListAPIView, CourseListApiView, LessonListApiView, CertificateListApiView, ReviewListApiView, CartItemsListApiView, FavoriteItemsListApiView


router = routers.SimpleRouter()
router.register(r'user', UserProfileListAPIView, basename='userprofile_crud')


urlspatterns = [
    path('', include(router.urls)),
    # path('', CategoryListAPIView.as_view(), name='movies'),
    # path('<int:pk>/', CategoryListAPIView.as_view(), name='movie_details'),
    ]