from django.contrib import admin
from .models import Pokemon

# Register your models here.


@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "hp", "active",)
    list_filter = ("active",)
    list_display_links = ("id", "name",)

    fieldsets = (
        ("general", {"fields": ("name", "hp", "active", "type",)}),
        ("localizations", {"fields": ("name_fr", "name_ar", "name_jp",)}),
    )
    # fieldssets has str and dictionary
