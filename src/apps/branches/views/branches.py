from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND

from apps.base.views.viewsets import CustomViewSet
from apps.branches.models.branch import BranchCompany
from apps.branches.serializers.branches import (BranchListSerializer, BranchCreateSerializer, BranchDetailSerializer,
                                                BranchUpdateSerializer)


class BranchListViewSet(CustomViewSet):
    # Lists all branch companies, requires authentication
    permission_classes = [IsAuthenticated]

    def list(self, request):
        queryset = BranchCompany.objects.all()
        serializer = BranchListSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BranchDetailViewSet(CustomViewSet):
    # Retrieves a specific branch by id_branch, requires authentication
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, id_branch):
        try:
            branch = BranchCompany.objects.get(id_branch=id_branch)
        except BranchCompany.DoesNotExist:
            return BranchCompany({'error': 'Branch not found!'}, status=HTTP_404_NOT_FOUND)

        serializer = BranchDetailSerializer(branch)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BranchCreateViewSet(CustomViewSet):
    # Creates a new branch, requires authentication
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = BranchCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchUpdateViewSet(CustomViewSet):
    # Partially updates a branch by id_branch, requires authentication
    permission_classes = [IsAuthenticated]

    def partial_update(self, request, id_branch):
        try:
            branch = BranchCompany.objects.get(id_branch=id_branch)
        except BranchCompany.DoesNotExit:
            return Response({'error': 'Branch object not found!'})

        serializer = BranchUpdateSerializer(branch, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BranchDeleteViewSet(CustomViewSet):
    # Deletes a branch by id_branch, requires authentication
    permission_classes = [IsAuthenticated]

    def destroy(self, request, id_branch):

        branch = BranchCompany.objects.get(id_branch=id_branch)
        branch.delete()
        return Response({'message': 'Branch Company successfully deleted!'})