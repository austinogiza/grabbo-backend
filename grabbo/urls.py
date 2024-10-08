from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
schema_view = get_schema_view(
   openapi.Info(
      title="Grabbo API",
      default_version='v1',
      description="Official API for Grabbo Fertility Clinic & Diagnostic Center",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@grabbofertilityclinic.com"),
      license=openapi.License(name="Grabbo Ferility Clinic & Diagnostic Center"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("clinic.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
