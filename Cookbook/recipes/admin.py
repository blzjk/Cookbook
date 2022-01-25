from django.contrib import admin
from django.utils.html import format_html
from .models import Recipes, Ingredients, Vote, Rating, Categories

# Register your models here.
admin.site.register(Rating)

class RatingInLine(admin.StackedInline):
    model = Rating

@admin.register(Recipes)
class RecipeAdmin(admin.ModelAdmin):
    inlines = [RatingInLine, ]
    list_display = ['title', 'description', 'category', 'date', 'show_url']
    list_filter = ['category', 'date']


    def show_url(self, obj):
        if obj.source is not None:
            return format_html(f'<a href="{obj.source}" target="_blank">{obj.source}</a>')
        else:
            return ''

    show_url.short_description = 'url'


@admin.register(Ingredients)
class IngredientAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ['recipe', 'reason']

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

#admin.site.register(Recipe, RecipeAdmin)
# admin.site.register(Ingredient)
# admin.site.register(Vote)
# admin.site.register(Rating)