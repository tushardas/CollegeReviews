# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from review.models import UserProfile,College,FileInfo
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from review.forms import UserForm,UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.staticfiles.templatetags.staticfiles import static
import json

def index(request):
    context = RequestContext(request)
    cred = UserProfile.objects.all()
    context_dict = {'credentials': cred}
    return render_to_response('review/index.html',context_dict)
    #return HttpResponse("College Review!!!")

def signup(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            registered = True

        else:
            print user_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response('review/signup.html',{'user_form':user_form, 'profile_form':profile_form,'registered':registered},context)
                
    
    
def user_login(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/review/')
            else:
                return HttpResponse("Your account is disabled")
        else:
            print "Invalid Login Credentials"
            return HttpResponse("Invalid Login Details")
    
    else:
        return render_to_response('review/login.html',{},context)


def view_review(request):
    
    context = RequestContext(request)
    flag = 1
    if request.method == "GET":
        search = request.GET['search']

        c = College.objects.filter(name = search)

        if len(c) != 0:
            name = c[0].name
            name = str(name)
            name = 'files/' + name + '.txt'
            k = FileInfo.objects.filter(filename=name)
            k = str(k[0].filename)
            f = open(k,"r")
            line = f.read()
            if(line is not None):
                return render_to_response('review/collreview.html',{'line':line, 'flag':flag},RequestContext(request))
            else:
                return render_to_response('review/collreview.html',{'line':line, 'flag':-1},RequestContext(request))
        else:
            flag = 0
            return render_to_response('review/collreview.html',{'flag':flag},context)


def add_coll(request):
    context = RequestContext(request)

    if request.method == 'POST':
        name = request.POST['name']
        location = request.POST['location']
        principles = request.POST['principles']

        obj = College(name=name,location=location,principles=principles)
        

        #file for storing review
        filename = 'files/' + name + '.txt'
        fd = open(filename,'w+')
        fd.close()
        
        obj.save()
        c = College.objects.filter(name=name)
        cid = int(c[0].id)
        fileobj = FileInfo(collname_id = cid, filename=filename)
        fileobj.save()
        f = FileInfo.objects.filter(filename = name)

        if len(f) != 0:
            return render_to_response('review/addcoll.html',{'flag':0,'name':name},context)
        
        else: return render_to_response('review/addcoll.html',{'flag':1,'name':name},context)
    
    else: return render_to_response('review/addcoll.html',{},context)


def add_review(request):
    context = RequestContext(request)
    
    if request.method == 'POST':
        collname = request.POST['name']
        review = request.POST['review']
        c = College.objects.filter(name=collname)
        collid = c[0].id
        fileinfo = FileInfo.objects.filter(collname=collid)
        filename = fileinfo[0].filename

        
        fd = open(filename,"a")
        fd.write("\n")
        fd.write(review)

    return render_to_response('review/addreview.html',{},context)