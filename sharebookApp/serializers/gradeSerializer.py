from sharebookApp.models.grade import Grade
from rest_framework import serializers

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['name_grade']