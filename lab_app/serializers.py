
from .models import lab_task_summary
from rest_framework import serializers


class lab_serializer(serializers.ModelSerializer):
     class Meta:
         model = lab_task_summary
         fields = ("name","age","research_type","equipments","findings","email")  