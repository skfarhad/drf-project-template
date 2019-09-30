from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

PROJECT_NAME = 'Project'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apidoc/', get_swagger_view(title=PROJECT_NAME + ' API Documentation')),
    path('v0/user/', include('apps.user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = PROJECT_NAME + " Admin"
admin.site.site_title = PROJECT_NAME + " Admin Portal"
admin.site.index_title = "Welcome to " + PROJECT_NAME + " Admin Portal"
