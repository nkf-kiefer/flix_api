from django.db import models

NATIONALITY_CHOICES = (
    ("USA", "American"),
    ("BRA", "Brazilian"),
    ("PER", "Peruvian"),
    ("ARG", "Argentinian"),
    ("CAN", "Canadian"),
    ("MEX", "Mexican"),
    ("COL", "Colombian"),
    ("CHI", "Chilean"),
    ("URU", "Uruguayan"),
    ("PAR", "Paraguayan"),
    ("BOL", "Bolivian"),
    ("VEN", "Venezuelan"),

    ("GBR", "British"),
    ("FRA", "French"),
    ("GER", "German"),
    ("ITA", "Italian"),
    ("ESP", "Spanish"),
    ("POR", "Portuguese"),
    ("NLD", "Dutch"),
    ("BEL", "Belgian"),
    ("SWE", "Swedish"),
    ("NOR", "Norwegian"),
    ("DNK", "Danish"),
    ("FIN", "Finnish"),

    ("RUS", "Russian"),
    ("TUR", "Turkish"),
    ("GRC", "Greek"),
    ("POL", "Polish"),
    ("CZE", "Czech"),
    ("HUN", "Hungarian"),

    ("CHN", "Chinese"),
    ("JPN", "Japanese"),
    ("KOR", "South Korean"),
    ("IND", "Indian"),
    ("IDN", "Indonesian"),
    ("PAK", "Pakistani"),

    ("AUS", "Australian"),
    ("NZL", "New Zealander"),

    ("ZAF", "South African"),
    ("NGA", "Nigerian"),
    ("EGY", "Egyptian"),

    ("ARG", "Argentine"),  # se quiser diferenciar do adjetivo
)


class Actor(models.Model):
    name = models.CharField(max_length=50)
    birthday = models.DateField(
        null=True, blank=True
    )  # permitindo deixar em branco o campo
    photo = models.ImageField(upload_to="actors_photos/")
    nationality = models.CharField(
        max_length=100, choices=NATIONALITY_CHOICES, blank=True, null=True
    )

    def __str__(self):
        return self.name
