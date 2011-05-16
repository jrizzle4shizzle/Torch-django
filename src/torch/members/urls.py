from django.conf.urls.defaults import *
from members.models import UserProfile

info_dict = {
    'queryset':UserProfile.objects.filter(user__is_active = True),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, paginate_by=25) ),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),
    (r'^(?P<object_id>\d+)/edit$', 'members.views.edit'),
)