from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

# Create your views here.
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # object have a lot of function. one of them is "all()"

        serializer = serializers.ImageSerializer(all_images, many=True) # var all_images translated Json

        return Response(data=serializer.data) # Save the translated file on the "data" variable 

class ListAllComments(APIView):

    def get(self, request, format=None):

        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)

        return Response(data=serializer.data)

class ListAllLikes(APIView):

    def get(self, request, format=None):

        all_likes = models.Like.objects.all()

        serializer = serializers.LikeSerializer(all_likes, many=True)

        return Response(data=serializer.data)