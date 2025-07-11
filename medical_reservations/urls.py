"""
URL configuration for medical_reservations project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from api.views import (
    AppointmentViewSet,
    DoctorViewSet,
    PatientViewSet,
    SpecialtyViewSet,
    appointment_schedule_view,
)

router = DefaultRouter()
router.register(r'specialties', SpecialtyViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'appointments', AppointmentViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title='Medical Reservations API',
        default_version='v1',
        description='App for managing medical appointments and reservations',
        terms_of_service='https://www.google.com/policies/terms/',
        contact=openapi.Contact(email='gooogle@gmail.com'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        'api/swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'api/appointments/schedule/',
        appointment_schedule_view,
        name='appointment_schedule',
    ),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
]
