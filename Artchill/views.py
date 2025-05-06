from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Canvas, Notes
from .serializers import CanvasSerializer , NotesSerializer 



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



class DrawingDetailView(APIView):

    def get_object(self,draw_id):
        return get_object_or_404(Canvas, id=draw_id)

    def get(self, request, draw_id):
        drawing = self.get_object(draw_id)
        serializer = CanvasSerializer(drawing)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, draw_id):
        drawing = self.get_object(draw_id)
        drawing.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


        
class NotesListCreateView(APIView):
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        content = request.data.get('content')

        if not content:
            return Response({"error": "Content is required."}, status=status.HTTP_400_BAD_REQUEST)

        serializer = NotesSerializer(data={'content': content})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

