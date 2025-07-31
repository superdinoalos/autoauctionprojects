<<<<<<< HEAD
from rest_framework import viewsets, filters
from .models import *
from .serializer import *
from django_filters.rest_framework import DjangoFilterBackend



class UserProfileViewSet(viewsets.ModelViewSet):
=======
from .serializer import UserProfileSerializer
from .models import UserProfile
from rest_framework import viewset



class UserProfileViewSet(viewset.ModelViewSet):
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


<<<<<<< HEAD
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]

    filterset_fields = ['brand', 'year', 'fuel_type']
    search_fields = ['model', 'description']
    ordering_fields = ['price', 'year', 'created_at']
    ordering = ['-created_at']


class AuctionViewSet(viewsets.ModelViewSet):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer


class BidViewSet(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
=======
class CarViewSet(viewset.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
