from django.contrib.auth.models import AbstractUser
from django.db import models 
from django.urls import reverse
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible  
class User(AbstractUser): #Extend from models

    """User Model"""

    GENDER_CHOICES = (
        ('male','Male'),
        ('female', 'Female'),
        ('not specified', 'Not Specified')
    ) 
    # First Name and Last Name do not cover name patterns
    # around the globe.
    profile_image = models.ImageField(null=True)
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    website = models.URLField(null=True)
    bio = models.TextField(null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
    followers = models.ManyToManyField("self") #When u have Foreignkey, u can choice only 1. but ManyToManyField can choice the 1 more 
    following = models.ManyToManyField("self")


    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
