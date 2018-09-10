# -*- coding:UTF-8 -*-

from django.db import models
from django.urls import reverse
from django.utils.six import python_2_unicode_compatible

# Create your models here.

@python_2_unicode_compatible
class Server_Type(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Server_URLs(models.Model):
	app_name = models.CharField(max_length=255)
	url = models.URLField(default="http://")
	description = models.CharField(max_length=255, blank=True, verbose_name='备注')
	required_database = models.TextField(blank=True, verbose_name='连接的数据库')
	required_api = models.TextField(blank=True, verbose_name='API调用')

	# 逻辑：
	# 规定一个内容只能对应一个环境，但是一个环境下可以有多个服务，所以使用 ForeignKey，服务和环境的关系为一对多的关联关系
	servertype = models.ForeignKey(Server_Type)
	def __str__(self):
		return self.app_name

	def get_absolute_url(self):
		return reverse('services:url_detail', kwargs={'pk': self.pk})

	class Meta:
		ordering = ['servertype', 'app_name']
		verbose_name = 'URL'
		verbose_name_plural = 'URL'

@python_2_unicode_compatible
class Elasticsearch_Node(models.Model):
	IP_Address = models.GenericIPAddressField()
	Node_Name = models.CharField(max_length=255)

	def __str__(self):
		return self.Node_Name