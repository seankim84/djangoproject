from django.db import models
from djangoproject.users import models as user_models #from to djangoproject/models/UserClass

class TimeStampModel(models.Model): # Like a bluePrint Model For other Models
    
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add : its automatically, whenever i want add something.
    updated_at = models.DateTimeField(auto_now=True) # self refresh

    class Meta(): # MetaClass: Anything that's not field.
        abstract = True # Now this Model, become a abstract base class.(this not related to database)
        # Like a AbstractUser. Helping the others model
# Create your models here.

    """Image Model"""

class Image(TimeStampModel): 
    
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField() # caption: 사진,잡화등에 붙인 정보
    creator = models.ForeignKey(user_models.User, null = True, on_delete=models.PROTECT)

    """Comment Model"""

class Comment(TimeStampModel):

    message = models.TextField()
    creator = models.name = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)

    """Like Model"""

class Like(TimeStampModel):

    creator = models.name = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image = models.name = models.ForeignKey(Image, null=True, on_delete=models.PROTECT)