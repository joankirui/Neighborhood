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
    health_tell = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.name}hood'

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,search_term):
        return cls.objects.filter(title__icontains=search_term)

# User class
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

class Business(models.Model):
    name = models.CharField(max_length=130)
    email = models.EmailField(max_length=255)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')
    neighborhood = models.ForeignKey('Neighborhood',on_delete=models.CASCADE, related_name='business')

    def __str__(self):
        return f'{self.name} Business'

class Post(models.Model):
    title = models.CharField(max_length=130, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='post_owner')
    hood = models.ForeignKey('NeighborHood', on_delete=models.CASCADE, related_name='hood_post')