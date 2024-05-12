from django.db import models
from django.contrib.auth.models import User
import datetime
from PIL import Image
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads/Medicine/')

    def __str__(self):
        return self.name

class Prescription(models.Model):
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    dosage = models.IntegerField(default=1)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=True)
    
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    first_name = models.CharField(max_length=255, default='')
    last_name = models.CharField(max_length=255, default='')
    phone_num = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    profile_image = models.ImageField(default='profile_images/default.svg', upload_to='profile_images')
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('pk',)
        verbose_name = 'patient'
        verbose_name_plural = 'patient'
    
    def get_absolute_url(self):
        return reverse('patient_detail', args=[str(self.id)])
    
    def __str__(self):
        return self.first_name



def save(self, *args, **kwargs):
    #super().save()

    img = Image.open(self.avatar.path)

    if img.height > 100 or img.width > 100:
        new_img = (100, 100)
        img.thumbnail(new_img)
        img.save(self.avatar.path)

def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Patient(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)