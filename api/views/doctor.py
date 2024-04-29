from rest_framework import viewsets, mixins
from rest_framework.response import Response

from api.filters import DoctorFilterSet
from api.models import Patient, Doctor
from api.serializers import *
from api.mixin import HospitalGenericViewSet
from django_filters.rest_framework import DjangoFilterBackend

class DoctorView(
                    HospitalGenericViewSet,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin
    ):
    lookup_field = 'id'
    filter_backends = [DjangoFilterBackend, ]
    filterset_fields = ['first_name', 'last_name', 'specialization']
    filterset_class = DoctorFilterSet

    def get_action_permissions(self):
        if self.action in ('list', 'retrieve'):
            self.action_permissions = ['view_doctor', ]
        elif self.action == 'list_patient':
            self.action_permissions = ['view_patient', ]
        else:
            self.action_permissions = []

    def get_serializer_class(self):
        if self.action == 'list':
            return DoctorListSerializer
        if self.action == 'retrieve':
            return DoctorRetrieveSerializer
        if self.action == 'create':
            return DoctorCreateSerializer
        if self.action == 'update':
            return DoctorUpdateSerializer
        if self.action == 'list_patient':
            return PatientListSerializer

    def get_queryset(self):
        if self.action == 'list_patient':
            return Patient.objects.prefetch_related('visits').all()

        return Doctor.objects.all()

    def list_patient(self, request, id):
        queryset = self.get_queryset().filter(visits__doctor__id=id)
        serializer = self.get_serializer(queryset, many=True)

        return Response(data=serializer.data)

#
# class ServiceViewSet(viewsets.GenericViewSet,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.UpdateModelMixin,
#                      mixins.DestroyModelMixin):
#     queryset = Service.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return ServiceListSerializer
#         if self.action == 'retrieve':
#             return ServiceDetailSerializer
#         if self.action == 'create':
#             return ServiceCreateSerializer
#         if self.action == 'update':
#             return ServiceUpdateSerializer
#
#
# class VisitViewSet(viewsets.GenericViewSet,
#                    mixins.ListModelMixin,
#                    mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin):
#     queryset = Visit.objects.all()
#
#     def get_serializer_class(self):
#         if self.action == 'list':
#             return VisitListSerializer
#         if self.action == 'retrieve':
#             return VisitDetailSerializer
#         if self.action == 'create':
#             return VisitCreateSerializer
#         if self.action == 'update':
#             return VisitUpdateSerializer