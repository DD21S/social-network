from rest_framework.routers import SimpleRouter

from comments.views import CommentViewSet

router = SimpleRouter()
router.register(r'comments', CommentViewSet)
