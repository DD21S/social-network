from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class ViewSetOptions(viewsets.ModelViewSet):
    """
    A viewset that provides the standard actions and like and dislikes options.
    """

    def create(self, request, pk=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            if 'post' in data:
                new_object = self.create_comment(request.user, data)
            else:
                new_object = self.create_post(request.user, data)
            serializer = self.serializer_class(new_object)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_image_or_none(self, data):
        image = None
        if 'image' in data:
            image = data['image']

        return image

    def create_post(self, user, data):
        image = self.get_image_or_none(data) 
        new_post = self.model_class(author=user, content=data['content'], image=image)
        new_post.save()

        return new_post

    def create_comment(self, user, data):
        image = self.get_image_or_none(data)
        new_comment = self.model_class(author=user, post=data['post'], content=data['content'], image=image)
        new_comment.save()

        return new_comment

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
