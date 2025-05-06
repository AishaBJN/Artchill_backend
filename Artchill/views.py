from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Canvas
from .serializers import CanvasSerializer

class CanvasListCreateView(APIView):
    def get(self, request):
        """fixed by ai"""
        canvases = Canvas.objects.order_by('-create_at') 
        serializer = CanvasSerializer(canvases, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        """fixed by ai"""
        title = request.data.get('title', 'Untitled')
        image_data = request.data.get('image_data', '')
        
        data = {
            'title': title,
            'image_data': image_data
        }
        
        serializer = CanvasSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)