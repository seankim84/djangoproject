from rest_framework import serializers
from djangoproject.images import serializers as images_serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):

    images = images_serializers.CountImageSerializer(many=True)

    class Meta:
        model = models.User
        fields = (
            'username',
            'name',
            'bio',
            'website',
            'post_count',       #from Model
            'following_count',  #from Model
            'followers_count',  #from Model
            'images',  
        )

class ListUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = (
            'id',
            'profile_image',
            'username',
            'name',
        )

