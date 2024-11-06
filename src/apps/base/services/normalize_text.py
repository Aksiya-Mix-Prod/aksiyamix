from django.db.models import CharField, Model, TextField


def normalize_txt(obj: Model):
    """Normalize text in CharField and TextFields"""
    for field  in obj._meta.get_fields():
        if isinstance(field, (CharField, TextField)):
            obj_field = getattr(obj, field.name, None)
            if obj_field:
                setattr(obj, field.name, ' '.join(obj_field.split()))