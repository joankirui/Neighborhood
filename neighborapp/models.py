from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=60)
    admin = models.ForeignKey('Profile',on_delete=models.CASCADE, related_name='hood')

    def __str__(self):
        return f'{self.name}hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,search_term):
        return cls.objects.filter(title__icontains=search_term)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    prof_pic = CloudinaryField('image')
    bio = models.CharField(max_length=30,blank=True,null=True)
    contact = models.EmailField(max_length=100)
    name = models.CharField(blank=True,max_length=100)
    location = models.CharField(blank=True,max_length=100)
    neighborhood = models.ForeignKey('NeighborHood', on_delete=models.SET_NULL, null=True, related_name='members', blank=True)

    def __str__(self):
        return f'{self.user.username}Profile'

    @receiver(post_save, sender=User)
    def create_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()