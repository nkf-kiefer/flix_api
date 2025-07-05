from actors.models import Actor
from rest_framework import generics
from actors.serializers import ActorSerializer
from rest_framework.permissions import (
    IsAuthenticated,
)  # importando uma classe de permissão
from app.permissions import GlobalDefaultPermission  # importando a permissão global


class ActorCreateListView(generics.ListCreateAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )  # a pessoa têm que passar por essa validação para conseguir listar e criar atores
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (
        IsAuthenticated,
        GlobalDefaultPermission,
    )
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
