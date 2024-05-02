from django.contrib import admin
from .models import Category, Medicine, Patient, Prescription
# Register your models here.
admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(Patient)
admin.site.register(Prescription)