from rest_framework import serializers
from . import models

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer): # Serializer have a Field like a Model Field

    comments = CommentSerializer(many=True)
    likes = LikeSerializer(many=True)

    class Meta: #Meta : Extra info
        model = models.Image
        fields = (
            'id',
            'file',
            'location',
            'caption',
            'comments',
            'likes',
        )

