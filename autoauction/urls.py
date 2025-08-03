from django.urls import path, include
from .views import *

from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'user', UserProfileViewSet, basename='users')
router.register(r'feedback', FeedbackListAPIView, basename='feedback')

urlpatterns = [
path('', include(router.urls)),
path('register/', RegisterView.as_view(), name='register'),
path('login/', CustomLoginView.as_view(), name='login'),
path('logout/', LogoutView.as_view(), name='logout'),
path('car/', CarListAPIView.as_view(), name='car_list'),
path('car/<int:pk>/', CarDetailAPIView.as_view(), name='car_detail'),
path('car/create/', CarCreateAPIView.as_view(), name='car_create'),
path('car_images/', CarImagesListAPIView.as_view(), name='car_images'),
path('brand/', BrandListAPIView.as_view(), name='brand_list'),
path('model/', ModelListAPIView.as_view(), name='model_list'),
path('aution/', AutionListAPIView.as_view(), name='aution_list'),
path('bid/', BidListAPIView.as_view(), name='bid_list'),



]