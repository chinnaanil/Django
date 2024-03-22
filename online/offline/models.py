from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class base(models.Model):
#     name=models.CharField( max_length=50)
#     age=models.IntegerField()
#     city=models.CharField( max_length=50)

class vote(models.Model):
    uid=models.ForeignKey(User, on_delete=models.CASCADE)
    vote_id=models.IntegerField()
    age=models.IntegerField()
    mandal=models.CharField( max_length=50)
    distic=models.CharField( max_length=50)
    state=models.CharField( max_length=50)