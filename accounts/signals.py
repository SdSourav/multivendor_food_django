from django.dispatch import receiver
from .models import User, UserProfile
from django.db.models.signals import post_save, pre_save


@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created: bool, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print('Profile created!')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('Profile updated!')
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
            print('Profile was not found, so it was created!')

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    print(f'{instance.username} is about to be saved!')
# post_save.connect(post_save_create_profile_receiver, sender=User)