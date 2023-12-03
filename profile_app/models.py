from django.db import models

# Create your models here.

class Profile (models.Model):
  name = models.CharField(max_length=250)
  image = models.ImageField(upload_to='profile_image')

    

  class Meta:
      verbose_name = ("Profile")
      verbose_name_plural = ("Profiles")

  def __str__(self):
      return self.name



    
