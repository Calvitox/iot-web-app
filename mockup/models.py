from django.db import models
from pymongo import MongoClient

class Con():
	c = MongoClient(host = '192.168.66.48', port = 27017)
	db = c.test