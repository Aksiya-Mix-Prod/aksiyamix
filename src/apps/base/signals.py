from django.dispatch import receiver
from django.db.models.signals import post_delete
from apps.base.services import delete_file_after_delete_obj


@receiver(post_delete)
def base_post_delete(instance, *args, **kwargs):
    """Deleting file after by object"""
    delete_file_after_delete_obj(instance)