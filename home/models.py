from django.db import models
from cloudinary.models import CloudinaryField
class Slider(models.Model):
    image = CloudinaryField('image')
    description = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=100, null=True)
    url = models.URLField(max_length=100, null=True)