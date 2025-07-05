from rest_framework import serializers
from movies.models import Movie
from django.db.models import Avg
from genres.serializers import GenreSerializer  # importando do serializers de genres
from actors.serializers import ActorSerializer  # importando do serializers de actors


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # Está olhando pro model de movies
        fields = "__all__"

    def validate_release_date(
        self, value
    ):  # fazendo uma validação do campo model release date
        if value.year < 1900:
            raise serializers.ValidationError(
                "A data de lançamento não pode ser anterior a 1900"
            )
        return value  # else retorna apenas o valor do ano

    def validate_resume(self, value):
        if len(value) > 500:  # len do valor do resumo
            raise serializers.ValidationError(
                "Resumo não deve ser maior que 500 caracteres"
            )
        return value


class MovieListDetailSerializer(serializers.ModelSerializer):  # serializer bonitoooo
    actors = ActorSerializer(many=True)  # pegando os atores
    genre = GenreSerializer()  # pegando os generos
    rate = serializers.SerializerMethodField(
        read_only=True
    )  # adicionando mais um campo no model para o serializer ler também

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "genre",
            "actors",
            "release_date",
            "rate",
            "resume",
        ]  # campos que eu quero

    def get_rate(
        self, obj
    ):  # media da avaliação do filme com base na nota que esta na REVIEWS
        rate = obj.reviews.aggregate(
            Avg("stars")
        )[
            "stars__avg"
        ]  # pegando do nosso obj Movie todas as reviews e criando um campo (aggregate) chamado stars__avg onde vai ter a média de stars

        if rate:  # se o filme tiver valor de rate ele mostra
            return round(rate, 1)
        return None  # se não fica nulo
