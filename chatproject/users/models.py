from django.db import models
from django.conf import settings

# Create your models here.
# user model

class Profile(models.Model):
  # add one to one field/relationship
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)

  def __str__(self):
    return self.user.username # typeerror

# TODO install pillow