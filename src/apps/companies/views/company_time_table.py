from apps.base.views.viewsets import CustomViewSet
from apps.companies.models.company_time_table import CompanyTimeTable
from apps.companies.serializers.company_time_table import (
    CompanyTimeTableCreateUpdateSerializer,
    CompanyTimeTableListSerializer,
    CompanyTimeTableRetrieveSerializer,
)
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class CompanyTimeTableListViewSet(CustomViewSet):
    """
    ViewSet for handling Company Time Table operations.
    """

    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["list"])
    def list(self, request):
        company_time_tables = CompanyTimeTable.objects.all()
        serializer = CompanyTimeTableListSerializer(company_time_tables, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyTimeTableRetrieveViewSet(CustomViewSet):
    """
    ViewSet to retrieve a specific company time able by its ID.
    """

    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk):
        try:
            time_table = CompanyTimeTable.objects.get(pk=pk)
        except CompanyTimeTable.DoesNotExist:
            return Response({"error": "CompanyTimeTable not found!"})

        serializer = CompanyTimeTableRetrieveSerializer(time_table)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CompanyTimeTableCreateViewSet(CustomViewSet):
    """
    Create a new company timetable.
    """

    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"])
    def create(self, request):
        serializer = CompanyTimeTableCreateUpdateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyTimeTableUpdateViewSet(CustomViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["patch"])
    def partial_update(self, request, pk):
        """
        Update a specific company timetable by its ID.
        """
        try:
            company_time_table = CompanyTimeTable.objects.get(pk=pk)
        except CompanyTimeTable.DoesNotExist:
            return Response({"error": "CompanyTimeTable not found!"})

        serializer = CompanyTimeTableCreateUpdateSerializer(
            company_time_table, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompanyTimeTableDeleteViewSet(CustomViewSet):
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=["delete"])
    def destroy(self, request, pk):
        """
        Delete a specific company timetable by its ID.
        """
        try:
            timetable = CompanyTimeTable.objects.get(pk=pk)
        except CompanyTimeTable.DoesNotExist:
            return Response(
                {"error": "Time table not found!"}, status=status.HTTP_404_NOT_FOUND
            )

        timetable.delete()
        return Response(
            {"message": "Time table successfully deleted!"},
            status=status.HTTP_204_NO_CONTENT,
        )
