from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Band(models.Model):

    def __str__(self) -> str:
        return f'{self.name}'
    
    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.CharField(max_length=100)
    genre = models.CharField(choices= Genre.choices, max_length=5)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2023)]
    )
    active = models.BooleanField(default=True)
    official_homepage = models.URLField(null=True, blank=True)


class Listing(models.Model):

    def __str__(self) -> str:
        return f"{self.title}"

    class ListingType(models.TextChoices):
        RECORDS = "disques"
        CLOTHING = "vêtements"
        POSTERS = "affiches"
        MISCELLANEOUS = "divers"

    title = models.CharField(max_length=100)
    desciption = models.CharField(max_length=1000)
    sold = models.BooleanField(default=False)
    year = models.IntegerField(null=True)
    type = models.CharField(choices = ListingType.choices, max_length=20)
    band =  models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
