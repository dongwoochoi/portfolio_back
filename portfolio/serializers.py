from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # 또는 ['id', 'writer', 'content', 'created_at'] 등 명시
