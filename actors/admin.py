from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)  # registrando no admin do django a classe Actor
class ActorAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "birthday",
        "photo",
        "nationality",
    )  # dados mostrados no admin
