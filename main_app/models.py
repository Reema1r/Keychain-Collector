# I used this resource to ceate material choices: https://www.geeksforgeeks.org/how-to-use-django-field-choices/?utm_source=chatgpt.com
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tag_name

class Keychain(models.Model):
    MATERIAL_CHOICES = [
        ("metal", "Metal"),
        ("plastic", "Plastic"),
        ("leather", "Leather"),
        ("wood", "Wood"),
        ("rubber", "Rubber"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100)
    acquired_in = models.CharField(max_length=100)
    year_acquired = models.PositiveIntegerField(default=2025)
    material = models.CharField(max_length=20, choices=MATERIAL_CHOICES, default="other")
    theme = models.CharField(max_length=100)
    story = models.TextField(max_length=500)
    is_gift = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name} - {self.acquired_in}"
    
    
    
class KeychainImage(models.Model):
    image = models.ImageField(upload_to='keychain_images/')
    caption = models.CharField(max_length=350)
    
    keychain = models.ForeignKey(Keychain, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.caption 
    
