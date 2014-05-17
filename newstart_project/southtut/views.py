from django.template import RequestContext
from django.shortcuts import render_to_response
from southtut.models import feed

def home(request):
    context = RequestContext(request)
    feed_list = feed.objects.all()
    context_dict = {'feeds': feed_list}
    return render_to_response('bootstrapTest/demo-077.html', context_dict, context)