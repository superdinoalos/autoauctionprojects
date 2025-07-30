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
]
