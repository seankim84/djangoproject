from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

# Create your views here.

class Feed(APIView):

    def get(self, request, format=None):

        user = request.user

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:
            
                image_list.append(image) # put in the image_list

        sorted_list = sorted(image_list, key=get_key, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)

def get_key(image):
    return image.created_at

class LikeImage(APIView):

    def post(self, request, image_id, format=None): #http request sending the data is post,put

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)
        
        except models.Image.DoesNotExist:
            return Response(status=404)
        
        new_like = models.Like.objects.create(
            creator = user,
            image = found_image
            )

        new_like.save()

        return Response(status=200)