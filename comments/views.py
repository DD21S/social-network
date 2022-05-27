from rest_framework.permissions import IsAuthenticated

from comments.models import Comment
from permissions.is_author_or_create_or_read_only import IsAuthorOrCreateOrReadOnly
from comments.serializers import CommentSerializer
from viewsets.viewset_options import ViewSetOptions

# Create your views here.

class CommentViewSet(ViewSetOptions):
    model_class = Comment
    permission_classes = [IsAuthenticated, IsAuthorOrCreateOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
