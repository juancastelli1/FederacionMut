from django.contrib import admin
from django.urls import path, re_path, include

from django.config import settings
from django.config.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    # re_path("", include("users.urls")),
    path("", include("Socios.urls")),
    path("", include("Farmacias.urls")),
    path("", include("Profesionales.urls")),
    path("", include("Medicamentos.urls")),
    path("", include("Ordenes.urls")),
    path("", include("Mutuales.urls")),
    path("", include("Cuotas.urls")),
    path("", include("Cobradores.urls")),
    path("", include("Estudios.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)