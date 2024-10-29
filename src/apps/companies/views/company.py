from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.base.views import CustomViewSet
from apps.companies.models.company import Company
from apps.companies.serializers.company import (CompanyListSerializer, CompanyCreateUpdateSerializer,
                                                CompanyRetrieveSerializer, CompanyDeleteSerializer)


class CheckUsernameViewSet(CustomViewSet):
    """
    ViewSet to check if a given username is available.
    """

    @action(detail=False, methods=['get'])
    def list(self, request):
        username = request.query_params.get('username', None)

        if not username:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        if Company.objects.filter(username=username).exists():
            return Response({'detail': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'detail': 'Username is available'}, status=status.HTTP_200_OK)


class CompanyListViewSet(CustomViewSet):
    """
    ViewSet to list all companies.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list(self, request):
        queryset = Company.objects.all()
        serializer = CompanyListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyRetrieveViewSet(CustomViewSet):
    """
    ViewSet to retrieve a specific company by its ID.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def retrieve(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanyRetrieveSerializer(company)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyCreateViewSet(CustomViewSet):
    """
    ViewSet to create a new company with the current user as owner.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create(self, request):
        serializer = CompanyCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyUpdateViewSet(CustomViewSet):
    """
    ViewSet to partially update a company's details by ID.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def partial_update(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CompanyCreateUpdateSerializer(company, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyDeleteViewSet(CustomViewSet):
    """
    ViewSet to delete a specific company by its ID.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['delete'])
    def delete(self, request, pk):
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return Response({'error': 'Company not found!'})

        serializer = CompanyDeleteSerializer(company)
        serializer.delete(company)
        return Response({'message': 'Company successfully deleted!'}, status=status.HTTP_204_NO_CONTENT)
