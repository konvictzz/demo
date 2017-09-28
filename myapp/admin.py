from django.contrib import admin
from .models import Article,UserInfo,Category,Tag,Article_Blog

# Register your models here.

#class ArticleAdmin(admin.ModelAdmin):
#	list_display = ('title', 'pub_date', 'update_time')
	#list_editable = ['title']
#	ordering = ['title']

class Article_BlogAdmin(admin.ModelAdmin):
	list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

#admin.site.register(Article,ArticleAdmin)
admin.site.register(UserInfo)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article_Blog, Article_BlogAdmin)