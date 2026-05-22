from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    level_display = serializers.CharField(source='get_level_display', read_only=True)
    
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'level', 'level_display', 'created_at']
        read_only_fields = ['id', 'created_at']