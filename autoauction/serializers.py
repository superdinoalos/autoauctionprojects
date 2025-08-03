from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = UserProfile
       fields = ('username', 'email', 'password', 'first_name', 'last_name',
                 'age', 'phone_number', 'status')
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = UserProfile.objects.create_user(**validated_data)
       return user


class LoginSerializer(serializers.Serializer):
   username = serializers.CharField()
   password = serializers.CharField(write_only=True)


   def validate(self, data):
       user = authenticate(**data)
       if user and user.is_active:
           return user
       raise serializers.ValidationError("Неверные учетные данные")


   def to_representation(self, instance):
       refresh = RefreshToken.for_user(instance)
       return {
           'user': {
               'username': instance.username,
               'email': instance.email,
           },
           'access': str(refresh.access_token),
           'refresh': str(refresh),
       }


class UseProfileSerializers(serializers.ModelSerializer):
   class Meta:
      model = UserProfile
      fields = '__all__'


class UseProfileSimpleSerializers(serializers.ModelSerializer):
   class Meta:
      model = UserProfile
      fields = ['first_name', 'last_name']



class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields =  '__all__'


class CarImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarImages
        fields = '__all__'

class CarListSerializer(serializers.ModelSerializer):
    seller = UseProfileSimpleSerializers()
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'seller', 'brand',
            'year', 'fuel_type', 'transmission', 'mileage', 'price',
        ]

class CarDetailSerializer(serializers.ModelSerializer):
    seller = UseProfileSimpleSerializers()
    model = ModelSerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    car_image = CarImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'car_image', 'seller', 'model', 'brand',
            'year', 'fuel_type', 'transmission', 'mileage', 'price', 'description'
        ]


class CarSerializer(serializers.ModelSerializer):
    seller = UseProfileSimpleSerializers()
    brand = BrandSerializer(read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'seller', 'brand',
            'year', 'fuel_type', 'transmission', 'mileage', 'price',
        ]



class AuctionSerializer(serializers.ModelSerializer):
    car_auctions =CarSerializer(many=True, read_only=True)

    class Meta:
        model = Aution
        fields = ['id', 'car_auctions', 'start_price', 'min_price', 'start_time', 'end_time', 'status']


class BidSerializer(serializers.ModelSerializer):
    buyer = UseProfileSimpleSerializers()

    class Meta:
        model = Bid
        fields = ['id', 'buyer', 'amount', 'created_add']


class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields =  '__all__'