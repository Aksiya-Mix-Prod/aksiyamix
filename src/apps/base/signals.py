from django.dispatch import receiver
from django.db.models.signals import post_delete
from apps.base.services import delete_file_after_delete_obj


@receiver(post_delete)
def delete_photo_on_delete_user(instance, *args, **kwargs):
    delete_file_after_delete_obj(instance)