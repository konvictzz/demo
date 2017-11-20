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
	url = models.URLField()
	description = models.CharField(max_length=255, blank=True)

	# 逻辑：
	# 规定一个内容只能对应一个环境，但是一个环境下可以有多个服务，所以使用 ForeignKey，服务和环境的关系为一对多的关联关系
	servertype = models.ForeignKey(Server_Type)
	def __str__(self):
		return self.app_name

	class Meta:
		ordering = ['servertype']
			