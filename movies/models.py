from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT, related_name="movies")
    release_date = models.DateField(null=True, blank=True)
    actors = models.ManyToManyField(Actor, related_name="movies")
    resume = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to="movies_photos/")

    def __str__(self):
        return self.title
