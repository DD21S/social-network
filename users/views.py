from rest_framework import mixins
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from permissions.is_self_or_read_only import IsSelfOrReadOnly
from users.models import User
from users.serializers import UserSerializer
from users.serializers import CreateUserSerializer
from users.serializers import DeleteUserSerializer

from posts.serializers import PostSerializer

@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(**serializer.validated_data) 
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  viewsets.GenericViewSet):
    """
    A viewset that provides `list`, `retrieve`, `update`, and `destroy` actions.
    """

    permission_classes = [IsAuthenticated, IsSelfOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def destroy(self, request, pk=None):
        serializer = DeleteUserSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_object()
            if user.check_password(serializer.validated_data.password):
                user.delete()
                return Response({"message": "user deleted."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def follow(self, request, pk=None):
        user = self.get_object()
        if user != request.user:
            if request.user in user.followers.all():
                return Response({"message": "You are already following this user."})
            user.followers.add(request.user)
            request.user.following.add(user)
            return Response({"message": "following"})
        return Response({"message": "You can't follow yourself."})

    @action(detail=True)
    def unfollow(self, request, pk=None):
        user = self.get_object()
        if request.user in user.followers.all():
            user.followers.remove(request.user)
            request.user.following.remove(user)
            return Response({"message": "Unfollowed"})
        return Response({"message": "You're not following this user."})

    @action(detail=True)
    def followers(self, request, pk=None):
        followers = self.get_object().followers.all()
        serializer = UserSerializer(followers, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data)
        return Response({"message": "Nothing here."})

    @action(detail=True)
    def following(self, request, pk=None):
        following = self.get_object().following.all()
        serializer = UserSerializer(following, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data)
        return Response({"message": "Nothing here."})

    @action(detail=True)
    def posts(self, request, pk=None):
        posts = self.get_object().post_set
        serializer = PostSerializer(posts, many=True)
        if len(serializer.data) > 0:
            return Response(serializer.data)
        return Response({"message": "Nothing here."})
