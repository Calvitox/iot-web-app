from django.db import models
from pymongo import MongoClient

class Con():
	c = MongoClient()
	db = c.blog

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=500)
    last_update = models.DateTimeField('date')