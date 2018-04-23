from rest_framework import serializers
from . import models

class ImageSerializer(serializers.Serializer): # Serializer have a Field like a Model Field

    class Meta: #Meta : Extra info
        model = models.Image
        fields = '__all__'

class CommentSerializer(serializers.Serializer):

    class Meta:
        model = models.Comment
        fields = '__all__'


class LikeSerializer(serializers.Serializer):

    class Meta:
        model = models.Like
        fields = '__all__'