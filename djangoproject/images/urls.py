from django.conf.urls import url
from . import views

app_name = "images" # Django 2.0 need it.
urlpatterns = [
    url(
        regex=r'^$',
        view=views.Feed.as_view(),
        name='feed'
    ),
    url(
        regex=r'(?P<image_id>[0-9]+)/like/', #if here request the <image_id>, u must write on the view argument "image_id"
        view=views.LikeImage.as_view(),
        name='like_image'
    ),
]