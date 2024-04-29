from rest_framework import serializers
from api.models import *

class PatientListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    date_of_birth = serializers.DateField()
    gender = serializers.CharField()

class PatientDetailedSerializer(PatientListSerializer):
    contact_info = serializers.CharField()


class PatientCreateOrUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


#
# class ServiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'
#
# class VisitSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = '__all__'
#
#
#
#
# class ServiceListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = ['id', 'name', 'cost']
# class ServiceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = '__all__'
#
# class ServiceCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         exclude = ['id']
#
# class ServiceUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Service
#         fields = ['name', 'description', 'cost']
#
#
#
#
#
# class VisitListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = ['id', 'doctor', 'patient', 'visit_date_time', 'status']
# class VisitDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = '__all__'
#
# class VisitCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         exclude = ['id']
#
# class VisitUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Visit
#         fields = ['doctor', 'patient', 'service', 'visit_date_time', 'status', 'notes']
