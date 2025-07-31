<<<<<<< HEAD
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'users', UserProfileViewSet)
router.register(r'cars', CarViewSet)
router.register(r'auctions', AuctionViewSet)
router.register(r'bids', BidViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
=======
from .views import *
from rest_framework.routers import SimpleRouter
from django.urls import path

router = routers.SimpleRouter()
router.register('user/', UserProfileViewSet, basename='users')
router.register('Car/', CarViewSet, basename='Car')


urlpatterns = [
    path('', include(router.urls))
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
]
