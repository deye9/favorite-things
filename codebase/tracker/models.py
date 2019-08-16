from django.db import models


class AuditLog(models.Model):
    model = models.CharField(max_length=30, blank=True)
    event = models.CharField(max_length=30)
    record_id = models.IntegerField(default=0)
    old_values = models.TextField()
    new_values = models.TextField()
    url = models.URLField()
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=30, null=True, blank=True)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)


class Category(models.Model):
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)


class Metadata(models.Model):
    key = models.CharField(max_length=30)
    value = models.CharField(max_length=30)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)


class Tracker(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=300, blank=True, null=True)
    ranking = models.IntegerField()
    metadata = models.ForeignKey(
        Metadata, related_name="tracker_metadata", on_delete=models.CASCADE, null=True)
    category = models.ForeignKey(
        Category, related_name="tracker_category", on_delete=models.CASCADE)
    created_date = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True)
