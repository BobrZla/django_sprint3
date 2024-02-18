from django.contrib import admin

from .models import Category, Location, Post


class PostInLine(admin.TabularInline):
    model = Post
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInLine,
    )
    list_display = (
        'title',
    )


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'is_published',
        'created_at',
        'category'
    )
    list_editable = (
        'is_published',
        'pub_date',
        'location',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Location)
admin.site.empty_value_display = 'Не задано'
