from django.contrib import admin
from backend.backend.models import Publication, Category


class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'tags', 'created_at')
    search_fields = ('title',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    search_fields = ('name',)


admin.site.register(Publication, PublicationAdmin)
admin.site.register(Category, CategoryAdmin)

