from members.models import UserProfile
from django.contrib.auth.models import User
from django.contrib import admin

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Contact Information', {'fields':['home_address_street', 'home_address_city','home_address_state', 'home_address_zip','home_phone_number', 'mobile_phone_number']}),
        ('Personal Information', {'fields':['birth_day', 'race', 'sex', 'ssn']}),
        ('Membership Information', {'fields':['membership_date','membership_type','committee', 'aaco_riding_db', 'badge_number', 'active_years_dues', 'life_insurance', 'administrative']}),
        ('Driver\'s License', {'fields':['drivers_license_number', 'drivers_license_state', 'drivers_license_class', 'drivers_license_expiration']}),
    ]
    list_display = ['user', 'membership_date']

admin.site.register(UserProfile, UserProfileAdmin)