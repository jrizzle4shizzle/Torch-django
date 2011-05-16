from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from django.contrib.localflavor.us.models import USStateField

# Create your models here.
class UserProfile(models.Model):
    home_address_street = models.CharField(blank=True, max_length = 255)
    home_address_city = models.CharField(blank=True, max_length = 50)
    home_address_state = USStateField(blank=True)
    home_address_zip = models.CharField(blank=True, max_length = 10)
    home_phone_number = PhoneNumberField(blank=True)
    mobile_phone_number = PhoneNumberField(blank=True)
    notes = models.TextField(blank=True)
    rank = models.TextField(blank=True)
    membership_type = models.TextField(blank=True)
    committee = models.TextField(blank=True)
    birth_day = models.DateField(null=True, blank=True)
    aaco_riding_db = models.BooleanField('AACO Riding Database', blank=True)
    badge_number = models.CharField(blank=True, max_length = 10)
    active_years_dues = models.BooleanField('Active year\'s dues paid', blank=True)
    life_insurance = models.BooleanField(blank=True)
    ssn = models.CharField('SSN', blank=True, max_length = 11)
    sex = models.CharField(blank=True, max_length = 6)
    race = models.CharField(blank=True, max_length = 20)
    drivers_license_number = models.CharField(blank=True, max_length = 50)
    drivers_license_state = USStateField(blank=True)
    drivers_license_class = models.CharField(blank=True, max_length = 25)
    drivers_license_expiration = models.DateField(null=True, blank=True)
    administrative = models.BooleanField(blank=True)
    membership_date = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, unique=True)
    
    def __unicode__(self):
        return self.user.username
    
    class Meta:
        permissions = (
            ("can_view_private", "Can view protected information"),
        )


    
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])