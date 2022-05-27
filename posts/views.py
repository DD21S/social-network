from rest_framework.permissions import IsAuthenticated

from posts.models import Post
from permissions.is_author_or_create_or_read_only import IsAuthorOrCreateOrReadOnly
from posts.serializers import PostSerializer
from viewsets.viewset_options import ViewSetOptions

# Create your views here.

class PostViewSet(ViewSetOptions):
    model_class = Post
    permission_classes = [IsAuthenticated, IsAuthorOrCreateOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
