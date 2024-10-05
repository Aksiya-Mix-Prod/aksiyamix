from django.db.models import FileField, ImageField, Model
from django.core.files.storage import default_storage


def delete_file_after_delete_obj(instance: Model):
    """Delete file after delete object"""
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name, None)
            if file_field and default_storage.exists(file_field.path):
                default_storage.delete(file_field.path)