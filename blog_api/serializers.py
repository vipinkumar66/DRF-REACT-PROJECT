from rest_framework import serializers

from blog.models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "author", "excerpt",
                  "content", "status")