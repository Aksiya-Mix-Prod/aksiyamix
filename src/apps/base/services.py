import os

from django.db.models import CharField, TextField, FileField, ImageField


def normalize_txt(obj):
    for field  in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name)
            if not obj_field is None:
                setattr(obj, field.name, ' '.join(obj_field.split()))


def delete_file_after_delete_obj(instance):
    for field in instance._meta.get_fields():
        if isinstance(field, (FileField, ImageField)):
            file_field = getattr(instance, field.name)
            if file_field and os.path.isfile(file_field.path):
                os.remove(file_field.path)