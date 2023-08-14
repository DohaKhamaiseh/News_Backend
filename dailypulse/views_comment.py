from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    UpdateAPIView

)
from rest_framework.permissions import IsAuthenticated
from .models import  Comment
from .permissions import IsOwnerOrReadOnly
from .serializers import CommentSerializer
from django.http import JsonResponse
from rest_framework.response import Response
import json

class Create_comment(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class Delete_comment(DestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly , IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)  # Perform the deletion

        remaining_data = Comment.objects.all()  # Retrieve the remaining data
        serializer = self.get_serializer(remaining_data, many=True)

        return Response(serializer.data)


class Get_comment_news(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    def get_queryset(self):
        title = self.kwargs['title']
        return Comment.objects.filter(newsTitle=title)

class Get_comment_user(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        news_id = self.kwargs['news_id']
        return Comment.objects.filter(user_id=user_id and news_id == news_id)

class Update_comment(UpdateAPIView):
    permission_classes = [IsOwnerOrReadOnly, IsAuthenticated]
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def update(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        body = json.loads(request.body)
        rowtobeupdated = Comment.objects.get(id = pk)
        rowtobeupdated.description = body["description"]
        rowtobeupdated.save()

        remaining_data = Comment.objects.all()  # Retrieve the remaining data
        serializer = self.get_serializer(remaining_data, many=True)

        return Response(serializer.data)
