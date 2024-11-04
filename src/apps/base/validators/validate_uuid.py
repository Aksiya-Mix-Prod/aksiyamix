import uuid

from apps.base.exceptions import CustomExceptionError


def validate_uuid(value):
    try:
        uuid.UUID(str(value))
    except ValueError:
        raise CustomExceptionError(code=400, detail={'error': f'{value} is not UUID'})