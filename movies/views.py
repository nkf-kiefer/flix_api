from rest_framework import generics, views, response, status
from movies.models import Movie
from movies.serializers import MovieModelSerializer, MovieListDetailSerializer
from rest_framework.permissions import IsAuthenticated
from app.permissions import GlobalDefaultPermission  # importando a permissão global
from django.db.models import Count, Avg
from reviews.models import Review


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Movie.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieListDetailSerializer
        return MovieModelSerializer


class MovieStatsView(
    views.APIView
):  # herdando de um tipo de classe que te da muita liberdade para alterar
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )  # autenticação de usuário
    queryset = Movie.objects.all()  # utilizando tudo da base de dados de movie

    # BUSCAR TODOS OS DADOS
    # MONTAR RESPOSTA
    # DEVOLVER RESPOSTA PRO USER COM ESTATISTICAS

    def get(self, request):  # definindo a lógica do get
        total_movies = self.queryset.count()  # total de filmes
        movies_by_genre = self.queryset.values("genre__name").annotate(
            count=Count("id")
        )  # quantos filmes tiveram de cada genero
        total_reviews = Review.objects.count()  # total de reviews que teve no banco
        average_stars = Review.objects.aggregate(avg_stars=Avg("stars"))[
            "avg_stars"
        ]  # media de estrelas de avaliações

        return response.Response(
            data={  # formatando a resposta json
                "total_movies": total_movies,
                "movies_by_genre": movies_by_genre,
                "total_reviews": total_reviews,
                "avarage_stars": round(average_stars, 1)
                if average_stars
                else 0,  # arredonando e deixando mais bonito
            },
            status=status.HTTP_200_OK,
        )
