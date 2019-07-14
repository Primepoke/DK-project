from django.contrib import admin
from .models import Post, Faq

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('topic_area', 'question', 'answer')
    search_fields = ('topic_area', 'question', 'answer')