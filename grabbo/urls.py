from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('grabbo/', include("clinic.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # re_path(".*", TemplateView.as_view(template_name="build/index.html")),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
