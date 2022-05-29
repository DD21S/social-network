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

@api_view(['POST'])
def create_user(request):
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        data = serializer.validated_data
        user = User.objects.create_user(**data) 
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
            user = get_object_or_404(User, pk=pk)
            if user.check_password(serializer.validated_data.password):
                user.delete()
                return Response({"message": "user deleted."})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True)
    def follow(self, request, pk=None):
        return Response({"message": "hello"})
