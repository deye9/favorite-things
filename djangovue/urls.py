from django.urls import path
from django.views.generic import TemplateView
from backend import views
from django.conf.urls import url

urlpatterns = [
    path('api/categories', views.CategoryView.as_view()),
    path('api/categories/<int:pk>', views.CategoryView.as_view()),

    path('api/metadata', views.MetadataView.as_view()),
    path('api/metadata/<int:pk>', views.MetadataView.as_view()),

    path('api/items', views.TrackerView.as_view()),
    path('api/items/<int:pk>', views.TrackerView.as_view()),

    path('api/logs', views.AuditLogView.as_view()),

    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
