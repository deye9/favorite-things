from tracker.models import Category, Metadata, Tracker, AuditLog
from tracker.serializers import CategorySerializer, MetadataSerializer, TrackerSerializer, AuditLogSerializer
from django.http import Http404
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class AuditLogView(APIView):
    def get(self, request, pk=None):
        if pk:
            auditlog = get_object_or_404(AuditLog.objects.all(), pk=pk)
            serializer = AuditLogSerializer(auditlog)
            return Response({"category": serializer.data})
        auditlogs = AuditLog.objects.all()
        serializer = AuditLogSerializer(auditlogs, many=True)
        return Response({"categories": serializer.data})

    def writeLog(self, model, event, pk, request=None, previousData=None):
        log = AuditLog()

        log.model = model
        log.event = event
        log.record_id = pk
        log.old_values = " " if request is None else request.data
        log.new_values = " " if request is None else request.data
        log.url = " " if request is None else request.path
        log.ip_address = "127.0.0.1" if request is None else request.META['REMOTE_ADDR']
        # request.META['HTTP_USER_AGENT'] if request.META['HTTP_USER_AGENT'] else request.META['user-agent']
        log.user_agent = " "
        log.created_date = datetime.now()
        log.save()
        return


class CategoryView(APIView):
    auditlog = AuditLogView()

    def get(self, request, pk=None):
        if pk:
            category = get_object_or_404(Category.objects.all(), pk=pk)
            serializer = CategorySerializer(category)
            return Response({"category": serializer.data})
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})

    def post(self, request):
        category = request.data

        # Create a category from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Category", "Insert", serializer.data['id'], request, serializer.data)
            return Response({"status": "success", "category": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_category = get_object_or_404(Category.objects.all(), pk=pk)
        serializer = CategorySerializer(saved_category, data=request.data)

        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Category", "Update", pk, request, CategorySerializer(saved_category).data)
            return Response({"status": "success", "Category": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        category = get_object_or_404(Category.objects.all(), pk=pk)
        category.delete()

        # create an audit log record
        self.auditlog.writeLog("Category", "Delete", pk, None, None)
        return Response({"status": "success", "message": "Category with id '{}' has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)


class MetadataView(APIView):
    auditlog = AuditLogView()
    
    def get(self, request, pk=None):
        if pk:
            metadata = get_object_or_404(Metadata.objects.all(), pk=pk)
            serializer = MetadataSerializer(metadata)
            return Response({"metadata": serializer.data})
        metadata = Metadata.objects.all()
        serializer = MetadataSerializer(metadata, many=True)
        return Response({"metadata": serializer.data})

    def post(self, request):
        category = request.data

        # Create a metadata from the above data
        serializer = MetadataSerializer(data=category)
        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Metadata", "Insert", serializer.data['id'], request, serializer.data)
            return Response({"status": "success", "metadata": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_metadata = get_object_or_404(Metadata.objects.all(), pk=pk)
        serializer = MetadataSerializer(saved_metadata, data=request.data)

        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Metadata", "Update", pk, request, MetadataSerializer(saved_metadata).data)
            return Response({"status": "success", "metadata": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        metadata = get_object_or_404(Metadata.objects.all(), pk=pk)
        metadata.delete()

        # create an audit log record
        self.auditlog.writeLog("Metadata", "Delete", pk, None, None)
        return Response({"status": "success", "message": "Metadata with id '{}' has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)


class TrackerView(APIView):
    auditlog = AuditLogView()

    def get(self, request, pk=None):
        if pk:
            item = get_object_or_404(Tracker.objects.all(), pk=pk)
            serializer = TrackerSerializer(item)
            return Response({"item": serializer.data})
        items = Tracker.objects.all()
        serializer = TrackerSerializer(items, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        category = request.data

        # Create a tracked item from the above data
        serializer = TrackerSerializer(data=category)
        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Tracker", "Insert", serializer.data['id'], request, serializer.data)
            return Response({"status": "success", "items": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        saved_tracker = get_object_or_404(Tracker.objects.all(), pk=pk)
        serializer = TrackerSerializer(saved_tracker, data=request.data)

        if serializer.is_valid():
            serializer.save()

            # create an audit log record
            self.auditlog.writeLog("Tracker", "Update", pk, request, TrackerSerializer(saved_tracker).data)
            return Response({"status": "success", "Tracker": serializer.data}, status=status.HTTP_200_OK)
        return Response({"status": "error", "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        # Get object with this pk
        tracker = get_object_or_404(Tracker.objects.all(), pk=pk)
        tracker.delete()

        # create an audit log record
        self.auditlog.writeLog("Tracker", "Delete", pk, None, None)
        return Response({"status": "success", "message": "Item with id '{}' has been deleted.".format(pk)}, status=status.HTTP_204_NO_CONTENT)
