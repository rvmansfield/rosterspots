from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    location = models.CharField(max_length=100,blank=True,null=True,default="")
    phone = models.CharField(max_length=50,blank=True,null=True,default="")
    email = models.CharField(max_length=50,blank=True,null=True,default="")

    def __str__(self):
        return f'{self.user.username} Profile'

# Automatically create/update the profile when the user is created/updated
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
