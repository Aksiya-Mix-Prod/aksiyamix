from django.db.models import FileField, ImageField, Model
from django.core.files.storage import default_storage


def delete_file_after_delete_obj(instance: Model):
    """Delete file after delete object"""
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name, None)
            if file_field and default_storage.exists(file_field.path):
                default_storage.delete(file_field.path)


def delete_file_after_update_obj(instance: Model):
    """Delete file after update object"""
    if not instance.pk:
        return
    
    old_instance = instance.__class__.objects.get(pk=instance.pk)

    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            old_file_field = getattr(old_instance, field.name, None)
            file_field = getattr(instance, field.name, None)
            if old_file_field and old_file_field != file_field and default_storage.exists(old_file_field.path):
                default_storage.delete(old_file_field.path)