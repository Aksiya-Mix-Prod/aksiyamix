from rest_framework.response import Response

from django.db.models import F

from apps.base.views.viewsets import CustomModelViewSet
from apps.companies.models import Company
from apps.companies.serializers.ratings import CompanyRatingSerializer


class CompanyRatingViewSet(CustomModelViewSet):
    """
    Create Rating of Company.
    """
    queryset = Company.objects.all()
    serializer_class = CompanyRatingSerializer

    def update_rating(self, company, rating):
        """
        Helper method to update rating counts based on user input.
        """

        rating_field = f'rating{rating}' #rating1, rating2, .... rating5
        setattr(company, rating_field, F(rating_field) + 1)

        company.rating_counts = str(int(company.rating_counts) + 1)

        total_weight_rating = (
            (company.rating1 * 1) +
            (company.rating2 * 2) +
            (company.rating3 * 3) +
            (company.rating4 * 4) +
            (company.rating5 * 5)
        )

        company.total_ratings = total_weight_rating / (company.rating_counts or 1)

        company.save()


    def create_rating(self, request, pk=None):
        """
        Endpoint for creating or updating a rating for a company.
        """
        company = self.get_object()
        rating = request.data.get('rating')

        if rating not in [1, 2, 3, 4, 5]:
            return Response({'error': 'Rating must be between 1 and 5'})

        self.update_rating(company, rating)

        serializer = self.get_serializer(company)
        return Response(serializer.data)
