# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from review.models import Credentials,College,FileInfo
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse
from review.forms import CredentialsForm

def index(request):
    content = RequestContext(request)
    cred = Credentials.objects.all()
    context_dict = {'credentials': cred}
    return render_to_response('review/index.html',context_dict)
    #return HttpResponse("College Review!!!")

def login(request):
    