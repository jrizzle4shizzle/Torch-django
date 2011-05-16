from django.conf.urls.defaults import *
from announcements.models import Announcement

info_dict = {
    'queryset':Announcement.objects.all(),
}

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.list_detail.object_list', dict(info_dict, paginate_by=25) ),
    (r'^(?P<object_id>\d+)/$', 'django.views.generic.list_detail.object_detail', info_dict),

)