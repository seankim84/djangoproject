from rest_framework import serializers
from . import models
from djangoproject.images import serializers as image_serializers
from djangoproject.users import serializers as user_serializers

class NotificationSerializer(serializers.ModelSerializer):

    creator = user_serializers.ListUserSerializer()
    image = image_serializers.SmallImageSerializer()

    class Meta:
        model = models.Notifications
        fields = "__all__"
