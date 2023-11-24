from django.db import models
from etc.uploader import Uploader
from etc.file_uploader import model2_image_uploader
# Create your models here.


class Model1(models.Model):
    img = models.ImageField(upload_to=Uploader('model1').model_image_uploader)

class Model2(models.Model):
    img = models.ImageField(upload_to=model2_image_uploader)
