from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Thumb_fr(models.Model):

    thumb1_img = models.ImageField(upload_to='pics')

class Thumb_sn(models.Model):

    thumb2_img = models.ImageField(upload_to='pics')

class Thumb_tr(models.Model):

    thumb3_img = models.ImageField(upload_to='pics')

class Recent(models.Model):
    
    recent_name = models.CharField(max_length=100)
    recent_img = models.ImageField(upload_to='pics')
    recent_file = models.FileField(upload_to='songs')

    def __str__(self):
        return self.recent_name

class Top(models.Model):
    
    top_name = models.CharField(max_length=100)
    top_img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.top_name

class Trend(models.Model):
    
    trend_name = models.CharField(max_length=100)
    trend_img = models.ImageField(upload_to='pics')
    trend_file = models.FileField(upload_to='songs')
    def __str__(self):
        return self.trend_name

class Artist(models.Model):
    
    artists_name = models.CharField(max_length=100)
    artists_img = models.ImageField(upload_to='pics')
    def __str__(self):
        return self.artists_name
