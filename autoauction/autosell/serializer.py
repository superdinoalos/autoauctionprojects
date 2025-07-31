<<<<<<< HEAD
from rest_framework import serializers
from .models import *
=======
from .models import *
from rest_framework import serializers
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
<<<<<<< HEAD
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class CarSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source='seller.username', read_only=True)

    class Meta:
        model = Car
        fields = [
            'id', 'brand', 'model', 'year', 'fuel_type', 'transmission',
            'mileage', 'price', 'description', 'seller', 'seller_username', 'created_at'
        ]
        read_only_fields = ['created_at']


class AuctionSerializer(serializers.ModelSerializer):
    car_info = serializers.StringRelatedField(source='car', read_only=True)

    class Meta:
        model = Auction
        fields = [
            'id', 'car', 'car_info', 'start_price', 'min_price',
            'start_time', 'end_time', 'status'
        ]


class BidSerializer(serializers.ModelSerializer):
    buyer_username = serializers.CharField(source='buyer.username', read_only=True)

    class Meta:
        model = Bid
        fields = ['id', 'auction', 'buyer', 'buyer_username', 'amount', 'created_at']
        read_only_fields = ['created_at']


class FeedbackSerializer(serializers.ModelSerializer):
    seller_username = serializers.CharField(source='seller.username', read_only=True)
    buyer_username = serializers.CharField(source='buyer.username', read_only=True)

    class Meta:
        model = Feedback
        fields = [
            'id', 'seller', 'seller_username', 'buyer', 'buyer_username',
            'rating', 'comment', 'created_at'
        ]
        read_only_fields = ['created_at']
=======
        fields = '__all__'


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
>>>>>>> e0bf5188d887d3d0c3a7fef246dafd8da9b23d35
