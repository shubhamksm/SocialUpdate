from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.shortcuts import reverse

# Create your models here.

class Post(models.Model):
	description = models.TextField(max_length=500)
	content_img = models.ImageField(upload_to='media/images/', blank=True)
	posted_at = models.DateTimeField(auto_now_add=True)
	liked = models.IntegerField(null=True)
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.description

	def get_absolute_url(self):
		return reverse('socialupdate-home')


class Comment(models.Model):
	message = models.TextField(max_length=200)
	posted_at = models.DateTimeField(auto_now_add=True)
	posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
	for_post = models.ForeignKey(Post, on_delete=models.CASCADE)	

	def __str__(self):
		return self.message

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	profile_pic = models.ImageField(upload_to='media/ProfilePictures/', blank=True, null=True)

	def __str__(self):
		return self.user.first_name
	
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
	instance.profile.save()