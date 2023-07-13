from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Role(models.Model):
    class Name(models.TextChoices):
        ADMIN = 'admin'
        WEB = 'web'
        STOCK = 'stock'
        MEMBRE = 'membre'
    
    name = models.CharField( max_length=300, choices=Name.choices)

    def __str__(self):
        return self.name


# MODEL USER
class User(AbstractUser):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)
    img_url = models.URLField(max_length=2000)
    newsletter = models.BooleanField(default=False)

    def __str__(self):
        return self.username 

