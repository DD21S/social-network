from comments.models import Comment
from comments.serializers import CommentSerializer
from viewsets.viewset_options import ViewSetOptions

# Create your views here.

class CommentViewSet(ViewSetOptions):
    model_class = Comment
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
