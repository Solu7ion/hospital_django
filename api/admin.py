from django.contrib import admin
from api.models import Specialization, Schedule,Visit, Patient, Service, Doctor

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Specialization)
admin.site.register(Visit)
admin.site.register(Patient)
admin.site.register(Service)
admin.site.register(Schedule)
