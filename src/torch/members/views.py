from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render_to_response, get_object_or_404
from members.models import UserProfile
from members.forms import UserProfileForm
from django.template import RequestContext 
from django.contrib.auth.decorators import login_required

@login_required
def edit(request, object_id):
    member = get_object_or_404(UserProfile, user__id = object_id)

    if request.user == member.user: 
        
        if request.method == "POST":
            form = UserProfileForm(request.POST, instance=member)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/members/'+object_id)
        else:
            form = UserProfileForm(instance=member)
        
        return render_to_response('members/edit.html', {'member_form':form, 'member':member},context_instance=RequestContext(request))
    
    else:
        return HttpResponse(status=403)
