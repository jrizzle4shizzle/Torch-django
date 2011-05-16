from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template import RequestContext 



@login_required
def index(request):
    return render_to_response('index/index.html',{},context_instance=RequestContext(request))
    