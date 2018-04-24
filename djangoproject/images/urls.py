from django.conf.urls import url
from . import views

app_name = "images" # Django 2.0 need it.
urlpatterns = [
    url(
        regex=r"^$",
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r"(?P<image_id>\w+)/like/",
        view=views.LikeImage.as_view(),
        name='like_image'
    )
]