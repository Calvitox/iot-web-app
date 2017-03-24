from django.db import models
from pymongo import MongoClient

class Con():
	c = MongoClient('http://192.168.66.48:27017')
	db = c.test