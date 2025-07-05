from rest_framework import serializers  # importando a biblioteca pronta de serializers
from genres.models import Genre  # importando o model que a gente vai trabalhar


class GenreSerializer(serializers.ModelSerializer):  # Criando um gênero serializer
    # defindo o model que ele vai utilizar
    class Meta:
        model = Genre
        fields = "__all__"  # campos do model que ele vai usar (no caso todos)
