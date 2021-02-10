from rest_framework import serializers
from .models import Manual, Practices


class ManualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manual
        fields = '__all__'


class PracticesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practices
        fields = '__all__'
