from urllib import request
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from mygallery1.models import *

def index(request):
    return render(request,'mygallery/index.html')

def signup(request): 
    res=render(request,'mygallery/signup.html')
    return res

def checkName(request):
    user=User.objects.filter(username=request.GET['username'])
    if not user:
        return HttpResponse('true')
    else:
        return HttpResponse('false')

def saveUser(request):
    user=User()
    user.username=request.POST['username']
    user.realname=request.POST['realname']
    user.emailid=request.POST['emailid']
    user.password=request.POST['password']
    user.save()
    return HttpResponseRedirect('http://localhost:8000/login')

def login(request):
    d1={}
    try:
        if request.GET['username']=='invalid':
            d1['errormsg']='Username Invalid'     
    except:
        d1['errormsg']=''
    try:
        if request.GET['password']=='invalid':
            d1['errormsg']='Password Invaild'
    except:
        pass
    res=render(request,'mygallery/login.html',d1)
    return res

def loginValidation(request):
    url=''
    try:
        user=User.objects.get(username=request.POST['username'])
        if user.username==request.POST['username'] and user.password==request.POST['password']:
            request.session['username']=user.username
            request.session['realname']=user.realname
            url='http://localhost:8000'
        else:
            url='http://localhost:8000/login?password=invalid'
    except:
        url='http://localhost:8000/login?username=invalid'
                
    return HttpResponseRedirect(url)

def logout(request):
    request.session.clear()
    return HttpResponseRedirect('http://localhost:8000/login')

def mygallery(request):
    gallery=Gallery.objects.filter(user=request.session['username'])
    video_obj=Video.objects.filter(user=request.session['username'])
    u=User.objects.get(username=request.session['username'])
    res=render(request,'mygallery/my_gallery.html',{'gallery':gallery,'video':video_obj,'realname':u})
    return res

def makegallery(request):
    res=render(request,'mygallery/make_gallery.html')
    return res

    
def saveGallery(request):
    url=''
    gallery=Gallery()
    gallery.title=request.POST['title']
    gallery.image=request.FILES['myimage']
    gallery.user=request.POST['userid']
    gallery.save()
    url='http://localhost:8000/my-gallery'
    return HttpResponseRedirect(url)

def viewPhoto(request):
    photo=Gallery.objects.get(id=request.GET['id'])
    u=User.objects.get(username=request.session['username'])
    res=render(request,'mygallery/photo.html',{'photo':photo,'username':u})
    return res

def deleteImage(request):
    g=Gallery.objects.get(id=request.GET['id'])
    g.delete()    
    return HttpResponseRedirect('http://localhost:8000/my-gallery')


def makevideo(request):
    return render(request,'mygallery/make_video.html')


def saveVideo(request):
    url=''
    video_obj=Video()
    video_obj.title=request.POST['title']
    video_obj.video=request.FILES['myimage']
    video_obj.user=request.POST['userid']
    video_obj.save()
    url='http://localhost:8000/my-gallery'
    return HttpResponseRedirect(url)


def viewvideo(request):
    video=Video.objects.get(id=request.GET['id'])
    u=User.objects.get(username=request.session['username'])
    res=render(request,'mygallery/video.html',{'video':video,'username':u})
    return res

def deletevideo(request):
    v=Video.objects.get(id=request.GET['id'])
    v.delete()    
    return HttpResponseRedirect('http://localhost:8000/my-gallery')