from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from apps.base.views.viewsets import CustomViewSet
from apps.branches.models.branch import BranchCompany
from apps.branches.serializers.branches import (BranchCreateSerializer,
                                                BranchDetailSerializer,
                                                BranchListSerializer,
                                                BranchUpdateSerializer)


class BranchListViewSet(CustomViewSet):
    """
    ViewSet to list all branches.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['get'])
    def list(self, request):
        """
        Lists all branches in the database.
        Fetches and serializes the queryset, returning the data in the response.
        """
        queryset = BranchCompany.objects.all()
        serializer = BranchListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BranchDetailViewSet(CustomViewSet):
    """
    ViewSet to retrieve a specific branch by id_branch.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def retrieve(self, request, id_branch):
        """
        Retrieves a branch by id_branch.
        Attempts to fetch a BranchCompany object with the provided id_branch.
        Returns a 404 response if the branch does not exist.
        """
        try:
            branch = BranchCompany.objects.get(id_branch=id_branch)
        except BranchCompany.DoesNotExist:
            return Response({'error': 'Branch not found!'}, status=status.HTTP_404_NOT_FOUND)

        serializer = BranchDetailSerializer(branch)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BranchCreateViewSet(CustomViewSet):
    """
    ViewSet to create a new branch.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['post'])
    def create(self, request):
        """
        Creates a new branch with the provided data.
        Validates the incoming data and saves the branch if valid.
        Returns validation errors if the data is invalid.
        """
        serializer = BranchCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchUpdateViewSet(CustomViewSet):
    """
    ViewSet to partially update a branch by id_branch.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['patch'])
    def partial_update(self, request, id_branch):
        """
        Partially updates a branch by id_branch.
        Attempts to fetch the branch with the given id_branch.
        Validates and saves the update if data is valid; returns validation errors if not.
        """
        try:
            branch = BranchCompany.objects.get(id_branch=id_branch)
        except BranchCompany.DoesNotExist:
            return Response({'error': 'Branch object not found!'})

        serializer = BranchUpdateSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDeleteViewSet(CustomViewSet):
    """
    ViewSet to delete a branch by id_branch.
    Requires authentication.
    """
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['delete'])
    def destroy(self, request, id_branch):
        """
        Deletes a branch by id_branch.
        Attempts to fetch and delete the branch with the given id_branch.
        Returns a success message if deleted, or a 404 error if the branch does not exist.
        """
        try:
            branch = BranchCompany.objects.get(id_branch=id_branch)
            branch.delete()
            return Response({'message': 'Branch Company successfully deleted!'},
                            status=status.HTTP_204_NO_CONTENT)
        except BranchCompany.DoesNotExist:

            return Response({'error': 'Branch not found!'}, status=status.HTTP_404_NOT_FOUND)


