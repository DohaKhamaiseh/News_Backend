from rest_framework import serializers
from .models import Dailypulse,Reading_later, Comment , News


class DailypulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailypulse
        fields = "__all__"

class ReadingLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading_later
        fields = "__all__"
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"
