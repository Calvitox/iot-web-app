from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
from mockup.models import Con
from bson.objectid import ObjectId
from bson.json_util import dumps
from django.views.decorators.csrf import csrf_exempt
import datetime
import pymongo
import json

connect = Con()

@api_view(['GET', 'POST'])
@csrf_exempt
def index(request): 
    # Get all posts from DB
    items =  connect.db.meta.find()
    items.sort([('dev_id', pymongo.ASCENDING)])
    items.limit(50)
    itemsJS = dumps(items)

    if request.method == 'POST':
        id = request.data.get('id')       
        if id != None:
            realid = id.split('_')[1]
            res =  connect.db.data.find({'dev_id':realid})
            res.sort([('dev_time', pymongo.ASCENDING)])
            dev = dumps(res)
            return Response(dev)
        else:
            return Response(itemsJS)
    else:
        return HttpResponse('REST SERVICE')
        #return render(request, 'index.html')
    