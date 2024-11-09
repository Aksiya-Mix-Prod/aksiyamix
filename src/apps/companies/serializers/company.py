from apps.base.serializers import CustomModelSerializer
from apps.categories.models import Category
from apps.companies.models.company import Company
from rest_framework import serializers


class CompanyBaseSerializer(CustomModelSerializer):
    """
    Base Serializer for Company mode.
    """

    class Meta:
        model = Company
        fields = [
            "owner",
            "categories",
            "owner_last_name",
            "owner_first_name",
            "owner_father_name",
            "owner_phone_number1",
            "owner_phone_number2",
            "logo",
            "video_url",
            "banner",
            "regions",
            "districts",
            "name",
            "username",
            "email",
            "address",
            "phone_number",
            "is_verified",
            "is_active",
            "is_deleted",
            "is_spammed",
            "id_company",
            "follower_counts",
            "like_counts",
            "dislike_counts",
            "comment_counts",
            "view_counts",
            "spam_counts",
            "branch_counts",
            "product_counts",
            "rating_counts",
            "active_discount_counts",
            "finished_discount_counts",
            "top_tariff_counts",
            "boost_tariff_counts",
            "discount_tariff_counts",
            "delivery",
            "installment",
            "short_description",
            "long_description",
            "web_site_url",
            "longitude",
            "latitude",
            "balance",
            "rating5",
            "rating4",
            "rating3",
            "rating2",
            "rating1",
        ]


class CompanyListSerializer(CompanyBaseSerializer):
    """
    List serializer for Company,
    Inherited from CompanyBaseSerializer.
    """

    class Meta:
        model = Company
        fields = [
            "id_company",
            "name",
            "username",
            "logo",
            "banner",
            "regions",
            "districts",
            "short_description",
            "rating_counts",
            "view_counts",
            "follower_counts",
            "like_counts",
            "is_verified",
        ]


class CompanyCreateUpdateSerializer(CompanyBaseSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), many=True, required=False
    )

    class Meta:
        model = Company
        exclude = (
            "id_company",
            "follower_counts",
            "like_counts",
            "dislike_counts",
            "comment_counts",
            "view_counts",
            "spam_counts",
            "branch_counts",
            "product_counts",
            "branch_counts",
            "rating_counts",
            "active_discount_counts"
            "finished_discount_counts"
            "top_tariff_counts"
            "boost_tariff_counts",
            "discount_tariff_counts",
            "balance",
            "rating5",
            "rating4",
            "rating3",
            "rating2",
            "rating1",
        )

        """
        Here we checking category in create time, because it`s M2MField
        """

        def create(self, validate_data):
            categories = validate_data.pop("category", [])
            company = Company.objects.create(**validate_data)
            company.category.set(categories)
            return company

        def update(self, instance, validate_data):
            categories = validate_data.pop("category", [])
            for (
                attrs,
                value,
            ) in validate_data.items():
                setattr(instance, attrs, value)

            instance.save()
            instance.category.set(categories)
            return instance

        def validate(self, attrs):
            model_clean = Company(**attrs)
            model_clean.clean()
            return attrs


class CompanyDeleteSerializer(CompanyBaseSerializer):
    class Meta:
        model = Company
        fields = ["id_company"]

        def delete(self, instance):
            instance.is_deleted = True
            instance.save()


class CompanyRetrieveSerializer(CompanyBaseSerializer):
    """
    Serializer for detailed company information.

    Fields:
        - `categories`: Lists related categories as strings.
        - `owner`: Shows the owner as a string.
        - `address_details`: Custom field for address info via `get_address()` from the Company model.

    Meta:
        - `model`: Company
        - `fields`: Includes various company attributes (owner, contacts, ratings, and location details).
    """

    address_details = serializers.SerializerMethodField()

    class Meta:
        model = Company
        fields = CompanyBaseSerializer.Meta.fields + ["address_details"]

    def get_address_details(self, obj):
        return obj.get_address()
