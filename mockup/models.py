from django.db import models
from pymongo import MongoClient

class Con():
	c = MongoClient()
	db = c.test