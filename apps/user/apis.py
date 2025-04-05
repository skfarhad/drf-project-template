from cProfile import Profile

from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from .models import User
from apps.common.apis import CustomViewSet, PaginatedResponse
from .serializers import ProfileSerializer


class ProfileViewSet(CustomViewSet):
    permission_classes = (IsAuthenticated,)
    ObjModel = User
    ObjSerializer = ProfileSerializer

    @extend_schema(
        summary="List all user profiles",
        description="Returns a list of all user profiles.",
        responses=ProfileSerializer()
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Retrieve a user profile",
        description="Returns the details of a specific user profile.",
        responses=ProfileSerializer()
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Create a new user profile",
        description="Creates a new user profile with the provided data.",
        request=ProfileSerializer,
        responses=ProfileSerializer()
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Partially update a user profile",
        description="Updates fields of an existing user profile.",
        request=ProfileSerializer,
        responses=ProfileSerializer()
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Paginated profile list",
        responses={200: PaginatedResponse(ProfileSerializer)}
    )
    @action(methods=['get'], detail=False)
    def paginated(self, request):
        return super().paginated(request)