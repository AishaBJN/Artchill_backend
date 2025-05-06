from django.urls import path
from .views import CanvasListCreateView,DrawingDetailView, NotesListCreateView

urlpatterns = [
    path('drawings/', CanvasListCreateView.as_view(), name='canvas-create'),
    path('drawings/<int:draw_id>/',DrawingDetailView.as_view(), name= 'draw_detail'),
    path('notes/',NotesListCreateView.as_view(), name= 'note_create'),
]