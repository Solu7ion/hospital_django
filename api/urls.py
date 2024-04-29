from django.urls import path
from api.views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path(
        'doctor/',
        DoctorView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'doctor/<int:id>',
        DoctorView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),
    path(
        'doctor/<int:id>/patient/',
        DoctorView.as_view({
            'get': 'list_patient',
        })
    ),



    # patient
    path(
        'patient/',
        PatientView.as_view({
            'get': 'list',
            'post': 'create'
        })
    ),
    path(
        'patient/<int:id>/',
        PatientView.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
        })
    ),

    path(
        'visit/',
        VisitView.as_view({
            'post': 'create'
        })
    ),

    # # Пути для ServiceViewSet
    # path(
    #     'services/',
    #     ServiceViewSet.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     }),
    #     name='service-list'
    # ),
    # path(
    #     'services/<int:pk>/',
    #     ServiceViewSet.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }),
    #     name='service-detail'
    # ),
    #
    # # Пути для VisitViewSet
    # path(
    #     'visits/',
    #     VisitViewSet.as_view({
    #         'get': 'list',
    #         'post': 'create'
    #     }),
    #     name='visit-list'
    # ),
    # path(
    #     'visits/<int:pk>/',
    #     VisitViewSet.as_view({
    #         'get': 'retrieve',
    #         'put': 'update',
    #         'delete': 'destroy'
    #     }),
    #     name='visit-detail'
    # ),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
