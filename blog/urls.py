from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Library Project",
        default_version='1.0.0',
        description="",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name=""),
    ),
    public=True,
    permission_classes=[permissions.IsAuthenticatedOrReadOnly],
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('frontend.urls')),
    path('api/user/', include('auth_app.urls')),
    path('api/posts/', include('post.urls')),
]
