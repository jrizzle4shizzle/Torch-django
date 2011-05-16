from django.db import models
from django.contrib.auth.models import User

class EventType(models.Model):
    name = models.CharField(blank=True, max_length=255)
    
    def __unicode__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(blank=True, max_length=255)
    date = models.DateField(null=True, blank=True)
    type = models.ForeignKey(EventType, blank=True)
    member_attending = models.ManyToManyField(User, blank=True)
    
    def __unicode__(self):
        return self.name
    
