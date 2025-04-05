from django.urls import path, re_path
from rest_framework import permissions
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView
)


from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

PROJECT_NAME = 'Project'

urlpatterns = [
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',SpectacularAPIView.as_view(), name='schema-json'
    ),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),

    # Swagger UI
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='schema-swagger-ui'),

    # ReDoc UI
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='schema-redoc'),


    path('admin/', admin.site.urls),
    path('v0/user/', include('apps.user.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = PROJECT_NAME + " Admin"
admin.site.site_title = PROJECT_NAME + " Admin Portal"
admin.site.index_title = "Welcome to " + PROJECT_NAME + " Admin Portal"
