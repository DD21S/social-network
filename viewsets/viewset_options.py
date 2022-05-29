from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from permissions.is_author_or_create_or_read_only import IsAuthorOrCreateOrReadOnly

class ViewSetOptions(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions and like and dislikes options.
    """

    permission_classes = [IsAuthenticated, IsAuthorOrCreateOrReadOnly]

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            new_object = self.create_new_object(request.user, data)
            serializer = self.serializer_class(new_object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def create_new_object(self, user, data):
        new_object = self.model_class(author=user, **data)
        new_object.save()

        return new_object

    @action(detail=True)
    def like(self, request, pk=None):
        selected_object = get_object_or_404(self.model_class, pk=pk)
        selected_object.liking()
        serializer = self.serializer_class(selected_object)
        return Response(serializer.data)

    @action(detail=True)
    def dislike(self, request, pk=None):
        selected_object = get_object_or_404(self.model_class, pk=pk)
        selected_object.disliking()
        serializer = self.serializer_class(selected_object)
        return Response(serializer.data)
