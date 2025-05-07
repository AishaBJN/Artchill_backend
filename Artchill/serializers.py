from rest_framework import serializers
from .models import Canvas, Notes





class CanvasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canvas
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'