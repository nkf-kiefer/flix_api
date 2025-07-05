from django.urls import path
from . import (
    views,
)  # para evitar ter que ficar escrevendo todas as views que estão la dentro

# como importou as views de maneira diferente têm que colocar views. antes do nome da view
urlpatterns = [
    path("genres/", views.GenreCreateListView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>/",
        views.GenreRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
]
