from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    fathersname = models.CharField(max_length=200)
    address = models.CharField(max_length=500)

    confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class EmailConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_link = models.CharField(max_length=33, primary_key=True)


class PasswordResetKeys(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    personal_link = models.CharField(max_length=33, primary_key=True)
