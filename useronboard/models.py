from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SignupForm(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    numberofdevices = models.CharField(max_length=200, null=True, blank=True)
    password = models.CharField(max_length=200)
    repassword = models.CharField(max_length=200)
    website = models.URLField(max_length=255, blank=True, null=True)
    profilepicture = models.ImageField(
        upload_to='profileimages', blank=True, null=True, default="images/userprofilepic.png")
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-edited_at', '-created_at']
        
    def __str__(self):
        return self.companyname
