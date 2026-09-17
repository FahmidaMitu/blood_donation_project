from django.contrib import admin
from .models import DonorProfile, BloodRequest

admin.site.register(DonorProfile)
admin.site.register(BloodRequest)