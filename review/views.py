# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from review.models import Coll,UserDetails,FileInfo
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from review.forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib.staticfiles.templatetags.staticfiles import static
import json
import datetime


def index(request):
    context = RequestContext(request)
    return render_to_response('review/index.html',context)

def view_review(request):
    request.session['collegename'] = ''
    context = RequestContext(request)
    flag = 1
    search = request.GET['search'].lower()
    request.session['collegename'] = search
    c = Coll.objects.filter(name = search)
    if len(c) != 0:
        club = c[0].clubs
        club = club.split(',')
        sport = c[0].sports
        sport = sport.split(',')
        name1 = c[0].name
        name = str(name1)
        name = 'files/' + 'uvce' + '.txt'
        #k = FileInfo.objects.filter(filename=name)
        #k = str(k[0].filename)
        f = open(name,"r")
        line = f.readlines()
        if(line is not None):
            name1 = name1.upper()
            return render_to_response('review/collreview.html',{'line':line, 'flag':flag, 'name':name1, 'club':club, 'sport':sport},RequestContext(request))
        else:
            return render_to_response('review/collreview.html',{'line':line, 'flag':-1},RequestContext(request))
    else:
        flag = 0
    return render_to_response('review/collreview.html',{'flag':flag},context)
    


def add_coll(request):
    context = RequestContext(request)
    if "username" in request.session:
        if request.method == 'POST':
            name = request.session['collegename']
            name = name.lower()
            location = request.POST['location']
            principles = request.POST['principles']
            
            obj = Coll(name=name,location=location,principles=principles)
            filename = 'files/' + name + '.txt'
            fd = open(filename,'w+')
            fd.close()
            obj.save()
            c = Coll.objects.filter(name=name)
            cid = int(c[0].id)
            fileobj = FileInfo(collname_id = cid, filename=filename)
            fileobj.save()
            f = FileInfo.objects.filter(filename = name)
            if len(f) != 0:
                 return render_to_response('review/addcoll.html',{'flag':0,'name':name},context)
            else: return render_to_response('review/addcoll.html',{'flag':1,'name':name},context)
    else: return render_to_response('review/reqlogin.html',{},context)
    if "collegename" in request.session:
        cname = request.session['collegename'].upper()
    return render_to_response('review/addcoll.html',{'name':cname},context)


def add_review(request):
    context = RequestContext(request)
    if "username" in request.session:
        #return render_to_response('review/reqlogin.html',{},context)
        if "collegename" in request.session:
            cname = request.session['collegename']
            cname = cname.upper()

        if request.method == 'POST':
            collname = request.session['collegename'].lower()
            review = request.POST['review']
            sports = request.POST['sports']
            clubs = request.POST['clubs']
            c = Coll.objects.get(name=collname)
            cid = c.id
            fileinfo = FileInfo.objects.filter(collname=cid)
            #filename = fileinfo[0].filename
            fd = open('files/uvce.txt',"a")
            fd.write(review)
            fd.write("\n")
            name = c.name    
            location = c.location
            principles = c.principles
            club = c.clubs + ',' + clubs
            sport = c.sports + ',' + sports
            c.delete()
            obj = Coll(name=name,location=location,principles=principles,clubs=club,sports=sport)
            obj.save()
        return render_to_response('review/addreview.html',{'name':cname},context)
    else:
        return render_to_response('review/reqlogin.html',{},context)

def register(request):
    context=RequestContext(request)
    if request.method=='POST':
        username = request.POST['username'].lower()
        email = request.POST['email']
        password = request.POST['password']
        confirm = request.POST['confirm']

        if password != confirm:
            return render_to_response('review/register.html',{'flag':-1},context)
        if username == '' or email == '' or password == '':
            return render_to_response('review/register.html',{'flag':-2},context)
        check = UserDetails.objects.filter(username=username)
        if check.count() != 0:
            return render_to_response('review/register.html',{'flag':-3},context)
        obj = UserDetails(username=username,email=email,password=password)
        obj.save()
        return render_to_response('review/register.html',{'flag':0},context)
    return render_to_response('review/register.html',{'flag':99},context)


def login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        u = UserDetails.objects.filter(username=username,password=password)
        if len(u) == 0:
            return render_to_response('review/signin.html',{'flag':-1},context)
        request.session['username'] = username
        return render_to_response('review/success.html',{'flag':0},context)
    return render_to_response('review/signin.html',{'flag':0},context)


def reqlogin(request):
    context = RequestContext(request)
    return render_to_response('review/reqlogin.html',{'flag':0},context)

def logout(request):
    context = RequestContext(request)
    del request.session['username']
    return render_to_response('review/index.html',{},context)

def list(request):
    context = RequestContext(request)

    c = Coll.objects.values_list('name')
    d = []
    for i in c:
        d.append(i[0].encode('ascii','ignore').upper())
    return render_to_response('review/list.html',{'college':d},context)