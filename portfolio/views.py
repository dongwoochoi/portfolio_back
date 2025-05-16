from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from rest_framework.decorators import api_view

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

@api_view(['POST'])
def create_post(request):
    writer = request.data.get("writer")
    content = request.data.get("content")
    return Response({"message": "저장 완료"}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def post_list(request):
    try: 
        posts = Post.objects.all().order_by('-created_at')
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)

    return Response(serializer.data)

# Create your views here.
