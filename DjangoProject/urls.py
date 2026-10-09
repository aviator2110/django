from django.contrib import admin
from django.urls import path, include
from notes import views as notes_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    #ADMIN AND SWAGGER:
    path("admin/", admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    #APPS:
    path("", notes_views.index, name="home"),
    path("about/", notes_views.about, name="about"),
    path("notes/", include("notes.urls")),
    path("accounts/", include("accounts.urls")),
    path('api/', include('api.urls')),
]
