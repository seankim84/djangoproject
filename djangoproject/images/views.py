from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers
# Create your views here.
class ListAllImages(APIView):

    def get(self, request, format=None):

        all_images = models.Image.objects.all() # object have a lot of function. one of them is "all()"

        serializer = serializers.ImageSerializer(all_images, many=True) # var all_images translated Json

        return Response(data=serializer.data) # Save the translated file on the "data" variable 