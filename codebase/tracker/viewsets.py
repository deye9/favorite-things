from rest_framework import viewsets, filters
from .models import Tracker
from .serializers import TrackerSerializer

class TrackerViewSet(viewsets.ModelViewSet):
    queryset = Tracker.objects.all()
    serializer_class = TrackerSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'title', 'description', 'category')
