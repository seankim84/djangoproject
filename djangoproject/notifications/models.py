from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangoproject.users import models as user_models
from djangoproject.images import models as image_models

@python_2_unicode_compatible
class Notifications(image_models.TimeStampedModel): #Call  TimeStampModel from Image Model 

    TYPE_CHOICES = (
        ('like','Like'),
        ('comment','Comment'),
        ('follow','Follow')
    )

    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='creator')
    to = models.ForeignKey(user_models.User, on_delete=models.PROTECT, related_name='to')
    notifications_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    image = models.ForeignKey(image_models.Image, null=True, blank=True, on_delete=models.PROTECT)
    comment = models.TextField(null=True, blank=True)

    class Meta:

        ordering = ['-created_at']

    def __str__(self):
        return '{} -To :{}'.format(self.creator, self.to)
    