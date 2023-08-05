from rest_framework import serializers
from .models import Dailypulse, Comment , News


class DailypulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailypulse
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
