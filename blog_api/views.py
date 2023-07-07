from rest_framework import generics
from rest_framework import permissions

from .serializers import PostListSerializer
from blog.models import Post

class PostUserWritePermissions(permissions.BasePermission):
    message = "Editing post is restricted to author only"
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author

class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostListSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermissions):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    permission_classes = [PostUserWritePermissions]

