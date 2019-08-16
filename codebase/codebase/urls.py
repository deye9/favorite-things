from django.urls import path
from tracker import views

urlpatterns = [
    path('api/categories', views.CategoryView.as_view()),
    path('api/categories/<int:pk>', views.CategoryView.as_view()),

    path('api/metadata', views.MetadataView.as_view()),
    path('api/metadata/<int:pk>', views.MetadataView.as_view()),

    path('api/items', views.TrackerView.as_view()),
    path('api/items/<int:pk>', views.TrackerView.as_view()),
]
