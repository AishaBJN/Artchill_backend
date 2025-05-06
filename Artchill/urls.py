from django.urls import path
from .views import CanvasListCreateView

urlpatterns = [
    path('drawings/', CanvasListCreateView.as_view(), name='canvas-list-create'),
]