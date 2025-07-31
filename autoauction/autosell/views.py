from .serializer import UserProfileSerializer
from .models import UserProfile
from rest_framework import viewset



class UserProfileViewSet(viewset.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class CarViewSet(viewset.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
