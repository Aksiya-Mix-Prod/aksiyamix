from rest_framework import serializers

from src.apps.companies.models.company import Company


class CompanyListSerializer(serializers.ModelSerializer):
    """
    Here doing list view
    """
    class Meta:
        model = Company
        fields = '__all__'


class CompanyCreateUpdateSerializer(serializers.ModelSerializer):
    """
    Here we are checking create of Company model
    """
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),
                                                  many=True, required=False)

    class Meta:
        model = Company
        exclude = ('id_generate', 'followers', 'likes', 'comments', 'views',
                   'rating5', 'rating4', 'rating3', 'rating2', 'rating1')

    """
    Here we checking category in create time, because it`s M2MField
    """
    def create(self, validated_data):
        categories = validated_data.pop('category', [])
        company = Company.objects.create(**validated_data)
        company.category.set(categories)
        return company

    def update(self, instance, validate_data):
        """
        Here checking Update part
        """
        categories = validate_data.pop('category', [])
        for attr, value in validate_data.items():
            setattr(instance, attr, value)

        instance.save()
        instance.category.set(categories)
        return instance

    def validate(self, attrs):
        """
        Custom validation for company model
        """
        model_clean = Company(**attrs)
        model_clean.clean()
        return attrs


class CompanyRetrieveSerializer(serializers.ModelSerializer):
    """
    Here checking Retrieve of 1 object.
    """
    class Meta:
        """
        In Retrieve user does not see this fields
        """
        model = Company
        exclude = ('rating5', 'rating4', 'rating3', 'rating2', 'rating1', 'longitude', 'latitude')