from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

class UserProfile(AbstractUser):
    username = models.CharField(max_length=100)
    STATUS_CHOICES = (
    ('seller', 'Seller'),
    ('buyer', 'Buyer')
    )
    phone_number = PhoneNumberField()

class Car(models.Model):
    FUEL_CHOICES = [
        ('petrol', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electric', 'Электро'),
        ('hybrid', 'Гибрид'),
    ]

    TRANSMISSION_CHOICES = [
        ('manual', 'Механика'),
        ('automatic', 'Автомат'),
        ('cvt', 'Вариатор'),
    ]

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=10, choices=FUEL_CHOICES)
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    mileage = models.PositiveIntegerField(help_text="Пробег в километрах")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cars')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"




