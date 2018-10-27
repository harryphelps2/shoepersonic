from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """Add extra details to user profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    marketing_opt_in = models.BooleanField(null=False, blank=False, default=False)
    profile_picture = models.ImageField(null=True, blank=True)
    running_club = models.CharField(max_length=50, null=True, blank=True) 
    achievements = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Automatically update user profile when a create event occurs.
    source: 'https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone'
    """
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """
    Automatically update user profile when a save event occurs.
    source: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
    """
    instance.profile.save()
