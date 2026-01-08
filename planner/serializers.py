from planner.models import StudySessions
from rest_framework import serializers
from .models import StudySessions

class StudySessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudySessions
        fields = '__all__'
