from rest_framework import routers
from tracker.viewsets import TrackerViewSet

router = routers.DefaultRouter()

router.register(r'item', TrackerViewSet)
