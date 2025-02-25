from rest_framework import serializers
from .models import TitleBasics

class TitleBasicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TitleBasics
        fields = '__all__'