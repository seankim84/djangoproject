from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangoproject.users import models as user_models #from to djangoproject/models/UserClass

@python_2_unicode_compatible
class TimeStampModel(models.Model): # Like a bluePrint Model For other Models
    
    created_at = models.DateTimeField(auto_now_add=True) #auto_now_add : its automatically, whenever i want add something.
    updated_at = models.DateTimeField(auto_now=True) # self refresh

    class Meta(): # MetaClass: Anything that's not field.
        abstract = True # Now this Model, become a abstract base class.(this not related to database)
        # Like a AbstractUser. Helping the others model
# Create your models here.

    """Image Model"""

@python_2_unicode_compatible
class Image(TimeStampModel): 
    
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField() # caption: 사진,잡화등에 붙인 정보
    creator = models.ForeignKey(user_models.User, null = True, on_delete=models.PROTECT, related_name='images')

    @property
    def like_count(self):
        return self.likes.all().count()
    
    def __str__(self): #You can find this on your image list
        return '{} - {}'.format(self.location, self.caption)

    class Meta: # configuring for Model.
        ordering = ["-created_at"] #Lastly order.

    """Comment Model"""

@python_2_unicode_compatible
class Comment(TimeStampModel):

    message = models.TextField()
    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='comments')
    #related_name = "This attribute specifies the name of the reverse relation from the User model back to your model." 

    def __str__(self):
        return '{} - {}'.format(self.message, self.creator)

    """Like Model"""

@python_2_unicode_compatible
class Like(TimeStampModel):

    creator = models.ForeignKey(user_models.User, null=True, on_delete=models.PROTECT)
    image = models.ForeignKey(Image, null=True, on_delete=models.PROTECT, related_name='likes')

    def __str__(self):
        return 'User: {} - Image Caption: {}'.format(self.creator.username, self.image.caption) 
        # At the ImageModel, Creator has the UserModel import already. so i can use the foreign key. 