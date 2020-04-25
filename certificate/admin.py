from django.contrib import admin
from .models import Firm, Profile, Certificate

# Register your models here.

admin.site.register(Firm)
admin.site.register(Profile)
admin.site.register(Certificate)
