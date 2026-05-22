from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'image', 'github_url', 'live_url', 'technologies', 'date_created', 'featured', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']