class AbstractCustomSerializerMixin:
    def save(self, **kwargs):
        user = self.context['request'].user
        if user.is_authenticated:
            if self.instance is None:
                kwargs['created_by'] = self.context['request'].user
            kwargs['updated_by'] = self.context['request'].user
        return super().save(**kwargs)