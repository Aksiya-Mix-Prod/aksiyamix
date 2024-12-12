from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from apps.base.services import (delete_file_after_delete_obj,
                                delete_file_after_update_obj)


@receiver(post_delete)
def base_post_delete(instance, *args, **kwargs):
    """Deleting file after by object"""
    delete_file_after_delete_obj(instance)


@receiver(pre_save)
def base_pre_save(instance, *args, **kwargs):
    """Deleting file after by object"""
    delete_file_after_update_obj(instance)
    