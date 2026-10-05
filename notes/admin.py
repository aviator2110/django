from django.contrib import admin
from notes.models import Category, Tag, Note


# Кусочек северо-атлантического лосося

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at', 'updated_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'author__username', 'content')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags',)
    readonly_fields = ('created_at', 'updated_at')