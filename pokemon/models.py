from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.


class Pokemon(models.Model):
    class PokemonType(models.TextChoices):
        WATER = "WA"
        GRASS = "GR"
        GHOST = "GH"
        STEEL = "ST"
        FAIRY = "FA"

    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30, choices=PokemonType.choices)

    hp = models.PositiveBigIntegerField(
        validators=[MaxLengthValidator(350), MinLengthValidator(50)])
    active = models.BooleanField(default=True)
    name_fr = models.CharField(max_length=30, default="")
    name_ar = models.CharField(max_length=30, default="")
    name_jp = models.CharField(max_length=30, default="")
    create_at = models.DateTimeField(auto_now_add=True)

    # run only one time
    modified_at = models.DateTimeField(auto_now=True)
    # to save any time when the is an update

    def __str__(self):
        return self.name  # to return the name when the admin is  inside
