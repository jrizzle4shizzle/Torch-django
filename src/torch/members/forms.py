from django.forms import ModelForm
from django.contrib.localflavor.us.forms import USZipCodeField
from members.models import UserProfile

class UserProfileForm(ModelForm):
    home_address_zip = USZipCodeField()
    class Meta:
        model = UserProfile
        fields = ('home_address_street', 'home_address_city', 'home_address_state', 'home_address_zip', 'home_phone_number', 'mobile_phone_number', 'drivers_license_number', 'drivers_license_state', 'drivers_license_class', 'drivers_license_expiration')
    