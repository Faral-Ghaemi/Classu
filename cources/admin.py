from django.contrib import admin
from . import models


@admin.register(models.Cource)
class CourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'school', 'category', 'price')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(models.Amoozeshgah)
class AmoozeshgahAdmin(admin.ModelAdmin):
    list_display = ('name',)
