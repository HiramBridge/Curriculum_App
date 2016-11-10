from django.contrib import admin
from .models import Category, Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
	list_display = ('tittle','text','posted','category')
	search_fields = ('tittle', 'category')


class CategoryAdmin(admin.ModelAdmin):
	list_display = ('tittle',)
	search_fields = ('tittle',)
	


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

