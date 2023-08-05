from rest_framework import serializers
from .models import Dailypulse,Reading_later


class DailypulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailypulse
        fields = "__all__"

class ReadingLaterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading_later
        fields = "__all__"
