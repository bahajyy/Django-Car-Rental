from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from datetime import datetime

class UserProfile(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.email

class Car(models.Model):
    TRANSMISSION_CHOICES = [
        ('Automatic', 'Automatic'),
        ('Manual', 'Manual'),
    ]

    brand = models.CharField(max_length=255, verbose_name='Brand', default='Unknown')
    model = models.CharField(max_length=255, verbose_name='Model', default='Unknown')

    city = models.CharField(max_length=255, verbose_name='City')
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES, verbose_name='Transmission')
    deposit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Deposit')
    mileage = models.PositiveIntegerField(verbose_name='Mileage')
    age = models.PositiveIntegerField(verbose_name='Age')
    cost_of_rental = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Cost of Rental')

    available_start_date = models.DateField(verbose_name='Available Start Date')
    available_end_date = models.DateField(verbose_name='Available End Date')

    photo = models.ImageField(upload_to='car_photos/', blank=True, null=True, verbose_name='Car Photo')

    def __str__(self):
        return f"{self.brand} {self.model} - {self.city} - {self.transmission} - {self.age}"

    @staticmethod
    def get_available_cars(start_date, end_date, city):
        return Car.objects.all()

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
