from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(
            user=user
        )
    else:
        profile = Profile.objects.get(user=user)
        profile.email = user.email
        profile.name = f"{user.first_name} {user.last_name}"
        profile.save()



@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user  # Accessing related user
        user.delete()  # Or whatever operation you're performing
    except User.DoesNotExist:
        # Handle the case where user does not exist
        pass

