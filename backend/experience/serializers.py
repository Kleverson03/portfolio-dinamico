from rest_framework import serializers
from .models import Experience

class ExperienceSerializer(serializers.ModelSerializer):
    type_display = serializers.CharField(source='get_type_of_experience_display', read_only=True)
    
    class Meta:
        model = Experience
        fields = ['id', 'title', 'company', 'description', 'type_of_experience', 'type_display', 'start_date', 'end_date', 'is_current', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']