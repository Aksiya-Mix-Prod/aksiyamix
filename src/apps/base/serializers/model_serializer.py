from rest_framework import serializers

from apps.base.serializers.abstract_serializer import \
    AbstractCustomSerializerMixin


class CustomModelSerializer(serializers.ModelSerializer, AbstractCustomSerializerMixin):
    pass