from rest_framework import serializers
from backend.models import AuditLog, Category, Metadata, Tracker


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MetadataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metadata
        fields = '__all__'


# class Ranking_Category_RelationshipSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Ranking_Category_Relationship
#         fields = '__all__'


class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracker
        fields = '__all__'
