from django.db import models

# conda activate djangodemo
# python manage.py makemigrations
# python manage.py migrate

# Create your models here.
class userinfo(models.Model):
    name = models.CharField(max_length=32)
    age = models.IntegerField()

