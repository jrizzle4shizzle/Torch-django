from django.db import models

# Create your models here.

class Announcement(models.Model):
    title = models.CharField(blank=False, max_length=255)
    text = models.CharField(blank=False, max_length=255)
    
    def __unicode__(self):
        return self.title