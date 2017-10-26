from django.contrib import admin
from services import models

# Register your models here.

class Server_URLsAdmin(admin.ModelAdmin):
	list_display = ['app_name','url','description','servertype']

#admin.site.register(Article,ArticleAdmin)
admin.site.register(models.Server_URLs, Server_URLsAdmin)
admin.site.register(models.Server_Type)