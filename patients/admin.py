from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Medicine, Patient, Prescription
# Register your models here.

class ProfileInline(admin.StackedInline):
    model=Patient

class UserAdmin(admin.ModelAdmin):
    model=User
    fields =['username']
    inlines= [ProfileInline]

admin.site.unregister(User)

admin.site.register(User, UserAdmin)
admin.site.register(Category)
admin.site.register(Medicine)
admin.site.register(Prescription)
