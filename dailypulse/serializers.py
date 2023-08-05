from rest_framework import serializers
from .models import Dailypulse, Comment


class DailypulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailypulse
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
