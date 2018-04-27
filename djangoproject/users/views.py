from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers

class ExploreUsers(APIView):

    def get(self, request, format=None):
        
        last_five = models.User.objects.all().order_by('-date_joined')[:5]

        serializer = serializers.ListUserSerializer(last_five, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)


class FollowUser(APIView):

    def post(self, request, user_id, format=None):

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExists: 
            return Respone(status=status.HTTP_404_NOT_FOUND)

        user.following.add(user_to_follow) # Add the "user_to_follow to following(list)"
        #it's easy to adding the elements at manyTomanyField.
        user.save()

        return Response(status=status.HTTP_200_OK)


class UnFollowUser(APIView):

    def post(self, request, user_id, format=None): #list에서 삭제하는것이기 때문에 delete를 사용할 필요가 없다.

        user = request.user

        try:
            user_to_follow = models.User.objects.get(id=user_id)
        except models.User.DoesNotExists: 
            return Respone(status=status.HTTP_404_NOT_FOUND)

        user.following.remove(user_to_follow) # remove the "user_to_follow to following(list)"
        #it's easy to removie the elements at manyTomanyField.
        user.save()

        return Response(status=status.HTTP_200_OK)

class UserProfile(APIView):
    def get(self, request, username, format=None):
        
        try: 
            found_user = models.User.objects.get(username=username)

        except models.User.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserProfileSerializer(found_user)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserFollowers(APIView):
    def get(self, request, username, format=None):
        
        try:
            found_user = models.User.objects.get(username=username)

        except models.User.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followers = found_user.followers.all()

        serializer = serializers.ListUserSerializer(user_followers, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

class UserFollowing(APIView):
    def get(self, request, username, format=None):

        try :
            found_user = models.User.objects.get(username=username)

        except models.User.DoesNotExists:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_followings = found_user.following.all()

        serializer = serializers.ListUserSerializer(user_followings, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
                