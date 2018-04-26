from rest_framework import serializers
from . import models
from djangoproject.users import models as user_models

class UserProfileImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Image
        fields = (
            'id',
            'file',
            'comment_count',
            'like_count',
        ) 


class FeedUserSerializer(serializers.ModelSerializer): 

    class Meta:
        model = user_models.User
        fields = (
            'username',
            'profile_image',   
        )

class CommentSerializer(serializers.ModelSerializer): #Serializer can also check saving
                                                      #Can generate something objects
    creator = FeedUserSerializer(read_only=True)

    class Meta:
        model = models.Comment
        fields = (
            'id', # id: Read Only Field.
            'message',
            'creator',
        )

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer): # Serializer have a Field like a Model Field

    comments = CommentSerializer(many=True) #Hidden Model. Declared at Model by related_name
    creator = FeedUserSerializer()

    class Meta: #Meta : Extra info
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'like_count', #from the property 
            'creator',
        )

