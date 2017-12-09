from django.contrib import admin
from rango.models import Category,Page
# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views', 'date')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'likes', 'views', 'slug', 'date')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
