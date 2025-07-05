from django.contrib import admin
from django.urls import (
    path,
    include,
)  # include serve para fazer uma varredura das urls dentro do caminho que você passou
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    # boa pratica de nome para APIS e versionamento das mesmas
    path("api/v1/", include("genres.urls")),
    path("api/v1/", include("actors.urls")),
    path("api/v1/", include("movies.urls")),
    path("api/v1/", include("reviews.urls")),
    path("api/v1/", include("authentication.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
