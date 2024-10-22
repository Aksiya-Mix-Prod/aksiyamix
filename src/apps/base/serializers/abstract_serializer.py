class AbstractCustomSerializerMixin:

    def create(self, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['created_by'] = validated_data['updated_by'] = user
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['updated_by'] = user
        return super().update(instance, validated_data)

    def save(self, **kwargs):
        user = self.context['request'].user
        if user.is_authenticated:
            if self.instance is None:
                kwargs['created_by'] = self.context['request'].user
            kwargs['updated_by'] = self.context['request'].user
        return super().save(**kwargs)