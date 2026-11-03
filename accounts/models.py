from django.db import models
from django.conf import settings
from django.core import validators
# from django.contrib.auth.models import User

class Country(models.Model):
    name = models.CharField(max_length=50)
    abbr = models.CharField(max_length=5)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'country'
        verbose_name = 'country'
        verbose_name_plural = 'countries'

# class State(models.Model):
#     country = models.ForeignKey(Country, related_name="%(class)s", on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)
    
# class City(models.Model):
#     state = models.ForeignKey(State, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     created_time = models.DateTimeField(auto_now_add=True)
#     updated_time = models.DateTimeField(auto_now=True)

class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='%(class)ss', on_delete=models.CASCADE)
    phone_number = models.BigIntegerField(blank=True, null=True, unique=True, 
                                          validators=[validators.RegexValidator(r'^989[0-39]\d{8}$')])
    country = models.ForeignKey(to=Country, related_name='%(class)s', on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, upload_to='profile_avatars/')


class Device(models.Model):
    DEVICE_WEB = 1
    DEVICE_IOS = 2
    DEVICE_ANDROID = 3
    DEVICE_WINDOWS = 4
    DEVICE_TYPE_CHOICE = (
        (DEVICE_WEB, 'web'),
        (DEVICE_IOS, 'ios'),
        (DEVICE_ANDROID, 'android'),
        (DEVICE_WINDOWS, 'windows'),
    )
    
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='%(class)ss', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(null=True)
    last_login = models.DateTimeField(null=True)
    device_type = models.PositiveSmallIntegerField(choices=DEVICE_TYPE_CHOICE, default=DEVICE_WEB)
    device_os = models.CharField(max_length=50, blank=True)
    device_model = models.CharField(max_length=50, blank=True)
    app_version = models.CharField(max_length=50, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'device'
        verbose_name = 'device'
        verbose_name_plural = 'devices'
        
        