from django.contrib import admin
from services import models

# Register your models here.

class Server_URLsAdmin(admin.ModelAdmin):
	fieldsets = (
		('Main', {
			'fields': ('servertype', 'app_name', 'url', 'description')
		}),
		('Advanced Options', {
			'classes': ('collapse',),
			'fields': ('required_database', 'required_api'),
		})
	)
	list_display = ['app_name','url','description','servertype']
	search_fields = ('required_database', 'required_api')
	empty_value_display = 'unknown'

#admin.site.register(Article,ArticleAdmin)
admin.site.register(models.Server_URLs, Server_URLsAdmin)
admin.site.register(models.Server_Type)
admin.site.register(models.Elasticsearch_Node)