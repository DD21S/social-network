from rest_framework.decorators import action
from rest_framework.response import Response

from posts.models import Post
from posts.serializers import PostSerializer
from viewsets.viewset_options import ViewSetOptions

from comments.serializers import CommentSerializer

# Create your views here.

class PostViewSet(ViewSetOptions):
    model_class = Post
    serializer_class = PostSerializer
    queryset = Post.objects.all()

    @action(detail=True)
    def comments(self, request, pk=None):
        comments = self.get_object().comment_set
        serializer = CommentSerializer(comments, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data)
        return Response({"message": "Nothing here."})
