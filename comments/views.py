from rest_framework import viewsets
from rest_framework import permissions

from .models import Comment
from .serializers import CommentSerializer

# Create your views here.

class CommentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows comment to be viewed or edited.
    """

    queryset = Comment.objects.all().order_by('-date_published')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
