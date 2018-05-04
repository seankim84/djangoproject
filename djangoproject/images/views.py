from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from djangoproject.users import models as user_models
from djangoproject.users import serializers as user_serializers
from djangoproject.notifications import views as notifications_views
from . import models, serializers

#get, post, put, delete etc..are functions which for the http_request

class Feed(APIView): #AS try,except u can match wether user is real user or not

    def get(self, request, format=None): # "format" parameter is used to define the output response format, like: csv, json, etc 

        user = request.user # it comes from Authentication middleware, give to us "User Object"

        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2]

            for image in user_images:

                image_list.append(image)

        my_images = user.images.all()[:2] #내가 방금 생성한 이미지도 피드에서 볼 수 있도록한다.

        for image in my_images:

            image_list.append(image)

        sorted_list = sorted(
            image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)

        return Response(serializer.data)

class LikeImage(APIView):

    def get(self, request, image_id, format=None): # 좋아요를 누른 모든 유저 리스트를 가져온다.
        
        likes = models.Like.objects.filter(image__id=image_id) # When Url give to the image_id, find the "like" which have image_id

        like_creators_ids = likes.values('creator_id') #U can extract the creator in "likes".

        users = user_models.User.objects.filter(id__in=like_creators_ids) # Searching the user id in array

        serializer = user_serializers.ListUserSerializer(users, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, image_id, format=None): #image_id : alredy declared on http parmeter. Call the ForeignKey of image

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)

        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try:
            preexisiting_like = models.Like.objects.get( #Restricting Like
                creator=user,
                image=found_image
            )
            return Response(status=status.HTTP_304_NOT_MODIFIED)

        except models.Like.DoesNotExist:

            new_like = models.Like.objects.create(
                creator=user,
                image=found_image
            )

            notifications_views.create_notifications(user, found_image.creator, 'like', found_image)

            new_like.save()

            return Response(status=status.HTTP_201_CREATED)

class UnLikeImage(APIView):

    def delete(self, request, image_id, format=None):
        
        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)

        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        try: 
            preexisiting_like = models.Like.objects.get(
                creator=user,
                image=found_image
            )
            preexisiting_like.delete()

            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Like.DoesNotExist:

            return Response(status=status.HTTP_304_NOT_MODIFIED)

class CommentOnImage(APIView):

    def post(self, request, image_id, format=None):

        user = request.user

        try:
            found_image = models.Image.objects.get(id=image_id)

        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.CommentSerializer(data=request.data) #To save the Serializer
        #request.data : returns the parsed content of the request body. This is similar to the standard request.POST and request.FILES
        if serializer.is_valid():

            serializer.save(creator=user)

            notifications_views.create_notifications(
                user, found_image.creator, 'comment', found_image, serializer.data['message'])

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Comment(APIView):

    def delete(self, request, comment_id, format=None):
        
        user = request.user

        try:
            comment = models.Comment.objects.get(id=comment_id, creator = user) #댓글 id는 url이어야 하고, 현재 삭제를 요청하는 유저와 같아야 삭제가능.
            comment.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        except models.Comment.DoesNotExist: 
            
            return Response(status=status.HTTP_404_NOT_FOUND)

class Search(APIView):

    def get(self, request, format=None):

        hashtags = request.query_params.get('hashtags', None)

        if hashtags is not None:

            hashtags = hashtags.split(",") # commma로 잘라서 array에 집어넣는다.

            images = models.Image.objects.filter(
                tags__name__in=hashtags).distinct() 
            #tags__name__in: django can search "Deep Relationship"
            #distinct: i don't wanna search twice.(중복된 값은 하나로만 표시)

            serializer = serializers.CountImageSerializer(images, many=True)

            return Response(data=serializer.data, status=status.HTTP_200_OK)

        else: 
            
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ModerateComments(APIView):

    def delete(self, request, image_id, comment_id ,format=None):
        
        user = request.user

        try:
            comment_to_delete = models.Comment.objects.get(
                id=comment_id, image__id=image_id, image__creator=user) #삭제하고자 하는 댓글의 id가 url의 id와 동일하고, 유저에의해 생성되었는지를 확인
            comment_to_delete.delete()

        except models.Comment.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(status=status.HTTP_204_NO_CONTENT)


class ImageDetail(APIView):

    def find_own_image(self, image_id, user): #self가 필요하다 해당 function은 class 안에 있기 때문에

        try: 
            image = models.Image.objects.get(id=image_id, creator=user) 
            return image
        except models.Image.DoesNotExist:
            return None

    
    def get(self, request, image_id, format=None):

        user = request.user

        try: 
            image = models.Image.objects.get(id=image_id, creator=user) #남이 만든것도 볼 수 있어야 하므로 creator=user를 제외한다.
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ImageSerializer(image)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, image_id, format=None): #When image update only can do created image by owner.

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None :

            return Response(status=status.HTTP_401_UNAUTHORIZED)
            

        try : 
            image = models.Image.objects.get(id=image_id, creator=user)
        except models.Image.DoesNotExist:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        serializer = serializers.InputImageSerializer(image, data=request.data, partial=True) #partial = 아직 serializer가 완벽히 update 되지 않아도 저장한다.

        if serializer.is_valid():

            serializer.save(creator=user)

            return Response(data=serializer.data, status=status.HTTP_204_NO_CONTENT)

        else :
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, image_id, format=None):

        user = request.user

        image = self.find_own_image(image_id, user)

        if image is None :

            return Response(status=status.HTTP_401_UNAUTHORIZED)

        image.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

