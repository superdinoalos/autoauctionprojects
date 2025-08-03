from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import viewsets, generics, status

from .filters import CarFilter
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .permissions import CreateCar

from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterView(generics.CreateAPIView):
   serializer_class = UserSerializer


   def create(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       serializer.is_valid(raise_exception=True)
       user = serializer.save()
       return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomLoginView(TokenObtainPairView):
   serializer_class = LoginSerializer


   def post(self, request, *args, **kwargs):
       serializer = self.get_serializer(data=request.data)
       try:
           serializer.is_valid(raise_exception=True)
       except Exception:
           return Response({"detail": "Неверные учетные данные"}, status=status.HTTP_401_UNAUTHORIZED)


       user = serializer.validated_data
       return Response(serializer.data, status=status.HTTP_200_OK)


class LogoutView(generics.GenericAPIView):
   def post(self, request, *args, **kwargs):
       try:
           refresh_token = request.data["refresh"]
           token = RefreshToken(refresh_token)
           token.blacklist()
           return Response(status=status.HTTP_205_RESET_CONTENT)
       except Exception:
           return Response(status=status.HTTP_400_BAD_REQUEST)


class UserProfileViewSet(viewsets.ModelViewSet):
   queryset = UserProfile.objects.all()
   serializer_class = UseProfileSerializers


   def get_queryset(self):
       return UserProfile.objects.filter(id=self.request.user.id)


class  ModelListAPIView(generics.ListAPIView):
    queryset = Model.objects.all()
    serializer_class = ModelSerializer


class  BrandListAPIView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class  CarListAPIView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarListSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = CarFilter
    search_fields = ['model']
    ordering_fields = ['price', 'year']


class  CarDetailAPIView(generics.RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarDetailSerializer


class  CarCreateAPIView(generics.CreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [CreateCar]


class  CarImagesListAPIView(generics.ListAPIView):
    queryset = CarImages.objects.all()
    serializer_class = CarImagesSerializer


class  AutionListAPIView(generics.ListAPIView):
    queryset = Aution.objects.all()
    serializer_class = AuctionSerializer


class  BidListAPIView(generics.ListAPIView):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer


class FeedbackListAPIView(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer