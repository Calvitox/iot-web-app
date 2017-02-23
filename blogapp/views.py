from django.shortcuts import render
from blogapp.models import Post, Con
from bson.objectid import ObjectId
import datetime
import logging

logger = logging.getLogger('django')

connect = Con()

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']
 
       post = {'title': title, 'content': content, 'last_update':datetime.datetime.now()}
       connect.db.entries.save(post)
 
    # Get all posts from DB
    posts =  connect.db.entries.find()
    return render(request,'index.html', {'Posts': posts})
 
 
def update(request):
    id = eval("request." + request.method + "['id']")
    objid = ObjectId(id)
    post = connect.db.entries.find_one({'_id':objid})
    logger.log(0,post)
    if request.method == 'POST':
        # update field values and save to mongo
        post['title'] = request.POST['title']
        post['last_update'] = datetime.datetime.now() 
        post['content'] = request.POST['content']
        connect.db.entries.save(post)
        template = 'index.html'
        params = {'Posts': connect.db.entries.find()} 
 
    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
    
    return render(request,template, params)
                               
 
def delete(request):
    id = eval("request." + request.method + "['id']")
 
    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 
 
    return render(request, template, params)

