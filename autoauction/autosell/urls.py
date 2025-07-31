from .views import *
from rest_framework.routers import SimpleRouter
from django.urls import path

router = routers.SimpleRouter()
router.register('user/', UserProfileViewSet, basename='users')
router.register('Car/', CarViewSet, basename='Car')


urlpatterns = [
    path('', include(router.urls))
]
