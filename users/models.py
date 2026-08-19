from django.db import models

    

class user(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    age = models.IntegerField()
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    languages = models.JSONField(default=list)
    

    

