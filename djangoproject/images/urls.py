from django.conf.urls import url
from . import views

app_name = "images" # Django 2.0 need it.
urlpatterns = [
    url(
        regex=r"^all/$",
        view=views.ListAllImages.as_view(),
        name='all_images'
    ),
    url(
        regex=r"^comments/$",
        view=views.ListAllComments.as_view(),
        name='all_comments'
    ),
    url(
        regex=r"^likes/$",
        view=views.ListAllLikes.as_view(),
        name='all_likes'
    )
]