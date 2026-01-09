from django.contrib import admin
from .models import Category


admin.site.register(Category)
class CateogryModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug' :('title',)}