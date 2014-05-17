from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = RequestContext(request)
    return render_to_response('bootstrapTest/index.html', context)

def home(request):
    context = RequestContext(request)
    return render_to_response('bootstrapTest/demo-077.html', {}, context)
