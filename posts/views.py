from posts.models import Post
from posts.serializers import PostSerializer
from viewsets.viewset_options import ViewSetOptions

# Create your views here.

class PostViewSet(ViewSetOptions):
    model_class = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()
