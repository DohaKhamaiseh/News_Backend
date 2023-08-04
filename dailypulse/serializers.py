from rest_framework import serializers
from .models import Dailypulse


class DailypulseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dailypulse
        fields = "__all__"
