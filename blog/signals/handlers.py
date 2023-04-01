from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from wagtail.signals import page_published
from ..models import Profile, ProfilePage


# @receiver(pre_save, sender=ProfilePage)
def create_profile_for_a_page(sender, **kwargs):
    instance = kwargs["instance"]

    if instance:
        # print(instance)
        Profile.objects.create(name=instance.name, bio=instance.bio)


@receiver(post_delete, sender=(ProfilePage))
def delete_page_profile(sender, **kwargs):
    instance = kwargs["instance"]
    if instance:
        Profile.objects.filter(name=instance.name).delete()


page_published.connect(create_profile_for_a_page,sender=ProfilePage)
