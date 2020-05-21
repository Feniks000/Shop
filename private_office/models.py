from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from showcase.models import Star


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, default='')
    lastname = models.CharField(max_length=200, default='')
    fathersname = models.CharField(max_length=200, default='')

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


class Order(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    star = models.OneToOneField(Star, on_delete=models.SET_NULL, null=True)

    star_name = models.CharField(max_length=200, default='')
    withdraw_amount = models.CharField(max_length=200, default='')
    operation_id = models.CharField(max_length=200, default='')
    unaccepted = models.CharField(max_length=200, default='')
    sha1_hash = models.CharField(max_length=200, default='')
    datetime = models.CharField(max_length=200, default='')
    currency = models.CharField(max_length=200, default='')
    building = models.CharField(max_length=200, default='')
    codepro = models.CharField(max_length=200, default='')
    street = models.CharField(max_length=200, default='')
    sender = models.CharField(max_length=200, default='')
    amount = models.CharField(max_length=200, default='')
    label = models.CharField(max_length=200, default='')
    suite = models.CharField(max_length=200, default='')
    city = models.CharField(max_length=200, default='')
    flat = models.CharField(max_length=200, default='')
    zip = models.CharField(max_length=200, default='')
